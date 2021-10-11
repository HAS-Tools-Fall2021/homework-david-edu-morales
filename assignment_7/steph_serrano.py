#%%
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

#%%
filename = 'streamflow_week7.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

#%%
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime'])

#%%
# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

#%%
#Week 1 Forecast:
def Week1_Forecast(month, startyear, data):

    '''Week 1 Forecast Summary: 
    
    This is going to give the median for a given day for a given year. Originally, this loop had an array for 31 days.
    I changed the range and storage to only provide data for one specific day in an overly complicated way.
    I am using the flow for October 11th, 2018 as my Week 2 Forecast because I have some thought that the year 2018 is similar, in terms of "wetness", to our current year. I am specifically using the 11th because USGS will update the flow Oct. 11th, 2021.'''

    Week1_Forecast = np.zeros(1)
    for x in range(1):
        daytemp = x + 11
        tempdata = data[(data['year']) & (data['month']) & (data['day'] == daytemp)]
        Week1_Forecast[x] = np.median(tempdata['flow'])
        print('Iteration', x, 'Day=', daytemp, 'Flow=', Week1_Forecast[x])

    return Week1_Forecast 

print(Week1_Forecast(10, 2018, data))

print(Week1_Forecast.__doc__)
 
#%%
#Week 2 Forecast:
def Week2_Forecast(month, startyear, data):
    '''Week 2 Forecast Summary: 
    
    Week 2 has similar reasoning as above except I used the Week 2 date (October 18th) for the year 2018 for my Week 2 forecast.
    This is why the daytemp = x+18.'''

    Week2_Forecast = np.zeros(1)
    for x in range(1):
        daytemp = x + 18
        tempdata = data[(data['year']) & (data['month']) & (data['day'] == daytemp)]
        Week2_Forecast[x] = np.median(tempdata['flow'])
        print('Iteration', x, 'Day=', daytemp, 'Flow=', Week2_Forecast[x])

    return Week2_Forecast

print(Week2_Forecast(10, 2018, data))

print(Week2_Forecast.__doc__)

#Plots to show flow for October, specifically in 2018:
#%%
#Scatter plot of Flow [cfs] vs Day for October:
oct_data = data[data['month']==10] 
fig, ax = plt.subplots()
ax.scatter(oct_data['day'], oct_data['flow'], alpha=0.2,
            s=0.02*oct_data['flow'], c=oct_data['year'], cmap='magma')
ax.set(yscale='log')
ax.set_xlabel('Day of the month')
ax.set_ylabel('Flow')
ax.set(title="Flow [cfs] vs. Day for October")
plt.show()

#%%
#October Daily Flows from 2008 to 2018:
mypal = sns.color_palette('magma', 12)
mypal
colpick = 0
fig, ax = plt.subplots()
for i in range(2008, 2019):
        plot_data=data[(data['year']==i) & (data['month'] == 10)]
        ax.plot(plot_data['day'], plot_data['flow'], color=mypal[colpick], label=i)
        ax.set(yscale='log')
        ax.legend()
        ax.set(title="Oct. Daily Flow from 2008-2018", xlabel="Day", ylabel="Daily Flow [cfs]")
        colpick = colpick + 1

#%%
#Time Series of Flow from Oct. 1st, 2018 to Oct. 31st, 2018.
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], label='Flow [cfs]')
ax.set(title="Observed Flow October 2018", xlabel="Date", ylabel="Weekly Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2018, 10, 1), datetime.date(2018, 10, 31)])
ax.legend()
plt.show()
# %%
