# %%
import os
import numpy as np
import pandas as pd

# %%
# Pulling data from streamflow15.txt
filename = 'streamflow_week15.txt'

# %%
# Read the data into a pandas df
data = pd.read_table(filename, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'])

# Expand the dates to year, month, day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)


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
# Look at the statistics of historical flows for Dec. 05-11 since 1989
flows_1989_to_2020 = add_dQ_df(historical_flow(data, 1989, 12, 5, 11))
week_stat(flows_1989_to_2020)

# %%
# Gather data for week 1 and 2 forecasts
wk1 = add_dQ_df(historical_flow(data, 2010, 12, 5, 11))
wk2 = add_dQ_df(historical_flow(data, 2010, 12, 12, 18))

# %%
# Print WEEKLY FORECASTS and stats for week 1 and week 2
week_stat(wk1, wk2)
print("\n------------------------\n\nWeek 1 forecast:",
      np.round(wk1.flow.mean(), 2), "\nWeek 2 forecast:",
      np.round(wk2.flow.mean(), 2))

# %%
