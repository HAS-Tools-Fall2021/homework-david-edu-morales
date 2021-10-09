# %%
# 1. Write a floop to calc. the avg flow for every day in Oct.
#2. do the same thing w/o using a floop
import os
import numpy as np
import pandas as pd

# %%
# You can start from the dataframe we have been creating for our homework
# Just make sure adjust the filepath accordingly
filename = 'streamflow_week2.txt'
filepath = os.path.join('../data', filename)
data = pd.read_table(filepath, sep='\t', skiprows=30,
                     names=['agency_cd', 'site_no',
                            'datetime', 'flow', 'code'],
                     parse_dates=['datetime']
                     )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

#%%
# 1) Write a floop to calc. the avg flow for every day in Oct.
flow_list = np.zeros(31)
for m in range(31):
    oct = data[(data.month == 10) & (data.day == (m+1))]
    day = oct.flow.mean()
    flow_list[m] = day

flow_list

# %%
# Dr. Condon's method.
flow_list = np.zeros(31)

for m in range(31):
    date = m+1

    oct = data[(data.month == 10) & (data.day == date)]
    flow_list[m] = np.mean(oct.flow)
    print('Iteration', m, 'Day=', date, 'Flow=', flow_list[m])


# %%
# 2) Method 2
oct_data = data[data['month'] == 10]
oct_data.groupby(['day'])[['flow']].mean()

# %%
# Class Exercise:
    # name = day_mean
    # Parameter; arg1 = month, arg2 = #days in that month, data to avg
    # Return => mean daily flows
def day_mean(month, days_of_month, data):
    flow_list = np.zeros(31)
    for m in range(days_of_month):
        date = m+1

        oct = data[(data.month == month) & (data.day == date)]
        flow_list[m] = np.mean(oct.flow)
        #print('Iteration', m, 'Day=', date, 'Flow=', flow_list[m])
    return flow_list

day_mean(10, 31, data)