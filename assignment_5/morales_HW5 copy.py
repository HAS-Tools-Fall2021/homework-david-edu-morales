# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# Set file location
filename = 'streamflow_week5.txt'
filepath = os.path.join('data', filename)
print(os.getcwd())
print(filepath)

filepath = '../data/streamflow_week5.txt'

# %%
# Read the data into a pandas dataframe
data = pd.read_table(filepath, sep = '\t', skiprows=30,
        names =['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] = data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

# %%
# 1.) Provide a summary of the dataframes properties (What are the column names?; 
#                                                     What is its index?;
#                                                     What dtypes does ea. column have?)
data.info()

# 2.) Provide summary of flow col. including: min; mean; max; std; and quartiles.
data["flow"].describe()

# 3.) Provide the same info but on monthly basis
data.groupby(["month"])[["flow"]].describe()

# 4.) Provide a table with 5 highest & 5 lowest flow values for the period of record.
#     Include the date, month, and flow values in summary.
flow_g2l = data[["datetime", "flow"]].sort_values(by="flow", ascending=False)
top5 = flow_g2l.head()
bot5 = flow_g2l.tail()

frames = [top5, bot5]
data_xtremes = pd.concat(frames)
data_xtremes

# 5.) Find the highest and lowest flow values for every month of the year
data.groupby(["year", "month"])[["flow"]].describe()

# 6.) Provide a list of historical dates with flows that are 
#     w/in 10% of one-week forecast values.
w1_prediction = 110

ten_pct = data[(data["flow"] >= 0.9*w1_prediction) & \
               (data["flow"] <= 1.1*w1_prediction)]
ten_pct_list = list(ten_pct.datetime)
len(ten_pct_list)
# %%
# Create new dataframe with relevant columns
flow_and_date = data[["year", "month", "day", "flow"]]
flow_and_date

# Create new dataframe with 'year' index
year_flow = flow_and_date.set_index("year")
year_flow

# Create overview of flow by month
overview_flow = flow_and_date.groupby(["month"])[["flow"]].describe()
overview_flow

# Create new dataframe with 'months' as index
month_flow = flow_and_date.set_index("month")
month_flow


# Create new dataframe for Sept. data
sept_flow = month_flow.loc[[9]]

test = sept_flow[sept_flow[""]]
## Set Sept. dataframe index to 'day'
sept_day_flow = flow_and_date.group

# Create overview of Sept. flow by year

# Isolate Sept. flows by week 09/27-10/03
late_sept = sept_flow[sept_flow["day"] >= 27]
late_sept

test = late_sept.groupby(["year"])[["flow"]].describe()
test
# %%
# Create Sept. specific data frame and reset index
sept_flow = flow_and_date[flow_and_date["month"] == 9]
sept_flow.reset_index(inplace=True)
sept_flow = sept_flow["year", "month", "day", "flow"]
sept_flow
# %%
