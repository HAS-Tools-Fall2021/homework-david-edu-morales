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
# ***********************************************************************************
# Data analysis used to obtain prediction:
# Create new dataframe with relevant columns and 'month' as index
month_flow = data[["year", "month", "day", "flow"]].set_index("month")

# Create new dataframe for Sept. data
sept_flow = month_flow.loc[[9]]

# Create new dataframe for Oct. data
oct_flow = month_flow.loc[[10]]

# Isolate Sept. flows by week 09/27-10/03
late_sept = sept_flow[sept_flow["day"] >= 27]
early_oct = oct_flow[oct_flow["day"] <= 3]

# %%
# Concatenate late sept and early oct flows into 'week1'
late_sept = late_sept.set_index("year")
early_oct = early_oct.set_index("year")
week1_frame = [late_sept, early_oct]

week1 = pd.concat(week1_frame)

# Find average flow of week1 by year
week1_yr = week1.groupby(["year"])[["flow"]].mean()

# Find average week1 of time period
#       Since 1989:
week1_yr.loc[1989:].mean()
#       Between 1989-2000
week1_yr.loc[1989:2000].mean()
#       Since 2010:
week1_yr.loc[2010:].mean()

# using week1_yr, make a graph of the results
f, ax = plt.subplots()

ax.bar(x=week1_yr.index,
       height=week1_yr.flow,
       color="green")
ax.set(title="Plot of Avg. Flow 9/27-10/3 since 1989")
plt.show()

# More analysis of 7-day flow by year:
wk1_analysis = week1.groupby(["year"])[["flow"]].describe()
wk1_analysis
# %%
