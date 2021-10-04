# Starter code for homework 5

# %%
# Import the modules we will use
import os
import numpy as np
from numpy.core.fromnumeric import mean
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
# Hints - you will need the functions: describe, info, groupby, sort, head and tail.
# Create new dataframe with relevant columns
flow_and_date = data[["year", "month", "day", "flow"]]
flow_and_date

# Create new dataframe with 'year' index
year_flow = flow_and_date.set_index("year")
year_flow

year_flow.loc[[1989], ["flow"]]

# Create overview of flow by month
overview_flow = flow_and_date.groupby(["month"])[["flow"]].describe()
overview_flow

# Create new dataframe with 'months' as index
month_flow = flow_and_date.set_index("month")
month_flow

# Create new dataframe for Sept. data
sept_flow = month_flow.loc[[9]]
sept_flow

# Create new dataframe for Oct. data
oct_flow = month_flow.loc[[10]]
oct_flow

# Create overview of Sept. flow by year
overview_sept_flow = sept_flow.groupby(["year"])[["flow"]].describe()
overview_sept_flow

# Isolate Sept. flows by week 09/27-10/03
late_sept = sept_flow[sept_flow["day"] >= 27]
late_sept
early_oct = oct_flow[oct_flow["day"] <= 3]
early_oct

# %%
# Concatenate late sept and early oct flows
late_sept = late_sept.set_index("year")
early_oct = early_oct.set_index("year")
test_frames = [late_sept, early_oct]
test_frames
test = pd.concat(test_frames)
test

test_view = test.groupby(["year"])[["flow"]].mean()
test_view
test_view.loc[1989:].mean()
# using test_view, make a graph of the results
test_view.plot(y="flow", use_index = True)
f, ax = plt.subplots()

ax.bar(x=test_view.index,
       height=test_view.flow,
       color="green")
ax.set(title="Plot of Avg. Flow 9/27-10/3 since 1989")
plt.show()

# %%
# Practicing with for loops
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=
wk1_avg=np.zeros(32)
for m in range(32):
        #get date range
        sept_days = data[(data['day'] >= 27) & (data['month'] == 9) & 
        (data['year'] == (1989+m))]
        oct_days = data[(data['day'] <= 3) & (data['month'] == 10) & 
        (data['year'] == (1989+m))]
        # extract flow values from dates
        floop_avg = ((sept_days['flow'].sum() + oct_days['flow'].sum())/7)
        wk1_avg[m] = floop_avg
        
print(wk1_avg)

sept_days.append(oct_days).info()       
# %%
