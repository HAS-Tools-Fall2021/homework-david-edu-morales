# This script assumes you have already downloaded several netcdf files
# see the assignment instructions for how to do this
# %%
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
# netcdf4 needs to be installed in your environment for this to work
import xarray as xr

# %%
filename = 'streamflow_week11.txt'
filepath = os.path.join('data', filename)

filepath = '../data/streamflow_week11.txt'

# %%
# Read the data into a pandas df
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'])

# Expand the dates to year, month, day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# Begin with HDF data
data_path = os.path.join('..', 'data',
                         'X70.176.149.188.310.12.14.57.nc')

# Read in the dataset as an x-array
dataset = xr.open_dataset(data_path)

# Focusing on just the specific humidity values
shum = dataset['shum']

# Grab data for just one point
lat = dataset["shum"]["lat"].values[0]
lon = dataset["shum"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
one_point = dataset["shum"].sel(lat=lat, lon=lon)

# use x-array to plot timeseries
one_point.plot.line()
precip_val = one_point.values

# Make a nicer timeseries plot
f, ax = plt.subplots(figsize=(12, 6))
one_point.plot.line(hue='lat',
                    ax=ax,
                    marker="o",
                    markersize=1.2,
                    linewidth=.1,
                    color="maroon",
                    markeredgecolor="chartreuse")

ax.set(title="Time Series For Specific Humidity at 35.2375N/247.5E\n"
             "from Jan. 1, 2001 - Nov. 6, 2021")

# Convert to dataframe
one_point_df = one_point.to_dataframe()

# %%
# Making a spatial map of one point in time
start_date = "2000-01-01"
end_date = "2000-01-01"

timeslice = dataset["shum"].sel(
    time=slice(start_date, end_date))

timeslice.plot()

# %%
# Create function for finding historical mean flows of desired timeframe
def historical_flow(data, start_year, start_month, start_day, end_day,
                    end_month=None):
    """Find yearly mean flow of chosen timeframe since chosen year.

    The timeframe will not cross years, it will only calculate dates within
    the same year. An upcoming edit that utilizes datetime will address this.

    This function uses a conditional to apply row extraction workflow depending
    on whether the timeframe extends across months. It then calculates their
    mean flow value for the week and adds it to a dataframe along with the
    values' corresponding year.

    Parameters
    ----------
    data : df
        dataframe from which to pull data
    start_year : int
        Year from which to begin timeframe
    start_month : int
        First month of flow in which the timeframe occurs
    start_day : int
        First day of the desired timeframe
    end_day : int
        Last day of the desired timeframe
    end_month : int (optional)
        Month in which the timeframe ends if it crosses month boundaries

    Returns
    ----------
    tf_avg_df : pandas dataframe
        Mean flow of timeframe and its year for every year since 1989
    """
    # generate lists that will receive looped year and flow values
    timeframe_avg_arr = []
    year_arr = []

    # calc number of iterations using start year
    df_year_range = data.groupby(['year']).describe()
    year_range = len(df_year_range.loc[start_year:])

    for year in range(year_range):

        # define year value that will be used in for_loop
        loop_year = start_year + year

        # capture date range if week overlaps month boundaries or not
        if end_month is None:
            month1 = data[(data['year'] == loop_year) &
                          (data['month'] == start_month) &
                          (data['day'] >= start_day) &
                          (data['day'] <= end_day)]
            # calc mean flow & add value to week_avg array
            tf_avg_value = np.round(np.mean(month1.flow), 2)

        else:
            month1 = data[(data['year'] == loop_year) &
                          (data['month'] == start_month) &
                          (data['day'] >= start_day)]
            month2 = data[(data['year'] == loop_year) &
                          (data['month'] == end_month) &
                          (data['day'] <= end_day)]
            # append dfs, calc mean flow & add to week_avg array
            tf_avg_value = np.round(np.mean(month1.append(month2).flow), 2)

        # add year and avg flow values to respective lists
        year_arr.append(loop_year)
        timeframe_avg_arr.append(tf_avg_value)

    # transfer lists into respective dataframes
    df1 = pd.DataFrame(year_arr)
    df2 = pd.DataFrame(timeframe_avg_arr)

    # concatenate dataframes into one and add col names
    tf_avg_df = pd.concat([df1, df2], axis=1)
    tf_avg_df.columns = ['year', 'flow']

    return tf_avg_df


# %%
# Function to calc change of flow (dQ)
def add_dQ_df(Qavg_df):
    """Calculate the change in mean flow of chosen timeframe from
    historical_mean() function and add it to dataframe.

    **The dataframe must have 0-based index,
      col1 = 'year', and col2 = 'flow'.**

    Parameters
    ----------
    Qavg_df : pandas dataframe
        Object assigned the output of historical_mean() function, or any df
        that fits the above bolded criteria.

    Returns
    ----------
    Qavg_df : pandas dataframe
        The output of this function is the same dataframe input with an added
        column, 'dQ', containing the change in mean flow between years.
    """
    # generate lists that will receive flow difference and looped year values
    flow_diff_arr = []
    flow_diff_year_arr = []

    # calc number of iterations by using df length
    years = len(Qavg_df)

    for i in range(years-1):

        # set year values
        new_year = i+1
        old_year = i

        # find difference in avg flow values (dQ)
        flow_diff = Qavg_df.iloc[new_year, 1] - Qavg_df.iloc[old_year, 1]

        # add year and flow diff values to respective lists
        flow_diff_year_arr.append(Qavg_df.iloc[new_year, 0])
        flow_diff_arr.append(flow_diff)

    # transfer lists to respective dataframes
    df1 = pd.DataFrame(flow_diff_year_arr)
    df2 = pd.DataFrame(flow_diff_arr)

    # concatendate dataframes into one and add col names
    dQ_df = pd.concat([df1, df2], axis=1)
    dQ_df.columns = ['year', 'dQ']

    dQ_df.loc[-1] = [1989, 0]
    dQ_df.index = dQ_df.index + 1
    dQ_df = dQ_df.sort_index()
    Qavg_df.insert(2, 'dQ', dQ_df.dQ)

    return Qavg_df


# %%
# Function to quickly generate plots (req'd 3)
def flow_analysis(Qavg_df):
    """Generate three plots to better undestand avg flow of timeframe.

    Parameters
    ----------
    Qavg_df : pandas dataframe
        Same output from add_dQ_df() function.

    Return
    ----------
    Plot1 : line chart
        Line chart of avg flow by year to identify long term patterns
        and changes.
    Plot2 : scatterplot
        Scatterplot of change in flow vs years.
    Plot3 : scatterplot
        Scatterplot of avg flow vs the change across years. Plot uses
        colorbar to aid understanding of changing patterns.
    """
    # line graph of the yearly mean flow for the dataframe's timeframe
    fig, ax = plt.subplots()

    ax.plot(Qavg_df['year'], Qavg_df['flow'], '-p', label='timeframe avg flow')
    ax.set(title="Mean Flow by Year", xlabel="Year",
           ylabel="Yearly Flow Rate Change [cfs/year]")
    ax.legend()

    # scatterplot of the change in mean flow across years
    fig, ax = plt.subplots()

    ax.plot(Qavg_df['year'], Qavg_df['dQ'], 'c')
    ax.set(title="Change in Mean Flow by Year", xlabel="Year",
           ylabel="\u0394Flow")
    ax.scatter(Qavg_df['year'], Qavg_df['dQ'],
               c=Qavg_df['year'], cmap=plt.cm.get_cmap('plasma'))

    # Scatterplot of avg flow vs rate of change
    fig, ax = plt.subplots()
    plt.scatter(Qavg_df.flow, Qavg_df.dQ,
                c=Qavg_df['year'], cmap='plasma')
    plt.colorbar()
    ax.set(xlabel="Mean Flow", ylabel="\u0394Flow",
           title="Mean Flow by Change in Mean Flow")

    return


# %%
# Function for quickly printing out stats for week dataframes
def week_stat(df1, df2=None):
    """Evaluate stats of up to two dataframes. Namely, the two
    one week forecasts.

    Parameters
    ----------
    df1 : pandas dataframe
        This argument is mandatory and provides the dataframe meant to
        be analyzed statistically.
    df2 : pandas detaframe (optional)
        This argument is meant to include a second forecast if the
        user so choses to include one; in the context of this assignment,
        the second dataframe is the two-week forecast.

    Return
    ----------
    Printed stats of the year, flow, and dQ column.
    """
    # Print out the Week 1 statistical information using a .describe() method.
    print("First DataFrame stats:\n", np.round(df1.describe(), 2),
          "\nFirst Dataframe median:", df1.flow.median())
    if df2 is not None:
        # Print out the Week 2 stats using a .describe() method.
        print("\nSecond DataFrame stats:\n", np.round(df2.describe(), 2),
              "\nSecond DataFrame median:", df2.flow.median())

    return


# %%
# Look at the statistics of historical flows for Nov. 7-13 since 1989
flows_1989_to_2020 = add_dQ_df(historical_flow(data, 1989, 11, 7, 13))
week_stat(flows_1989_to_2020)

# %%
# Explore long term patterns of flow for Nov. 6-13 since
# 1989 through graphs
flow_analysis(flows_1989_to_2020)

# %%
# Gather data for week 1 and 2 forecasts
wk1 = add_dQ_df(historical_flow(data, 2010, 11, 7, 13))
wk2 = add_dQ_df(historical_flow(data, 2010, 11, 14, 20))

# %%
# Print WEEKLY FORECASTS and stats for week 1 and week 2
week_stat(wk1, wk2)
print("\n------------------------\n\nWeek 1 forecast:",
      np.round(wk1.flow.mean(), 2), "\nWeek 2 forecast:",
      np.round(wk2.flow.mean(), 2))

# %%
# Explore week 1 and 2 flows graphically
flow_analysis(wk1)
flow_analysis(wk2)

# %%
