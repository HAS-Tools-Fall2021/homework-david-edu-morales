# Starter code for week 6 illustrating how to build an AR model 
# and plot it

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
#note you may need to do pip install for sklearn

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week6.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)


# %%
#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code'],
        parse_dates=['datetime']
        )

# Expand the dates to year month day
data['year'] = pd.DatetimeIndex(data['datetime']).year
data['month'] = pd.DatetimeIndex(data['datetime']).month
data['day'] = pd.DatetimeIndex(data['datetime']).day
data['dayofweek'] = pd.DatetimeIndex(data['datetime']).dayofweek

# %% 
# Here are some examples of things you might want to plot to get you started:

# 1. Timeseries of observed weekly flow values
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], '-k', label='daily')
ax.set(title="Observed Flow", xlabel="Date", 
        ylabel="Daily Avg Flow [cfs]",
        yscale='log')
ax.legend()
# an example of saving your figure to a file
fig.set_size_inches(5,3)
fig.savefig("Observed_Flow.png")

# %%
#************************************************************************
#2. Time series of flow values with the x axis range limited
fig, ax = plt.subplots()
ax.plot(data['datetime'], data['flow'], 'c')
ax.set(title="Observed Flow since 2015", xlabel="Date", ylabel="Daily Avg Flow [cfs]",
        yscale='log', xlim=[datetime.date(2015, 1, 1), datetime.date(2020, 10, 10)])
plt.show()

# %%
#***********************************************************************
#3 Boxplot of flows by Oct 4-10 since 2010
oct_time = data[(data['month'] == 10) & (data['year'] >= 2010)]
oct_days = oct_time[(oct_time['day'] >= 4) & (oct_time['day'] <= 10)]

fig, ax = plt.subplots()
ax = sns.boxplot(x=oct_days['day'], y="flow",  data=data,
                 linewidth=0.3)
ax.set(xlabel='Oct. Days', ylabel='Flow(cfs)', yscale='log')

plt.show()

# %%
#***********************************************************************
month_flow = data[["year", "month", "day", "flow"]].set_index("month")

# Create new dataframe for Oct. data
oct_flow = month_flow.loc[[10]]

# Isolate Sept. flows by week 09/27-10/03
oct = oct_flow[(oct_flow["day"] >= 4) & (oct_flow["day"] <= 10)]

# Concatenate late sept and early oct flows into 'week1'
early_oct = oct.set_index("year")

# Find average flow of week1 by year
week1_yr = early_oct.groupby(["year"])[["flow"]].mean()

# using week1_yr, make a graph of the results
f, ax = plt.subplots()

ax.bar(x=week1_yr.index,
       height=week1_yr.flow,
       color="green")
ax.set(title="Plot of Avg. Flow 10/4-10 since 1989", xlabel='Year', 
       ylabel='Flow (cfs)')
plt.show()

# %%
#***********************************************************************
# Figure out std
test = data.groupby(['year', 'month'])[['flow']].describe()
std = test['flow', 'std']
std.set_index('month')
test
f, ax = plt.subplots()

ax.bar(x=std[''],
       height=test['flow', 'std'],
       color="green")
ax.set(title="Plot of Avg. Flow 9/27-10/3 since 1989")
plt.show()

# %%
#**********************************************************************
# 4. Plot the september flows for the last 10 years
f, ax = plt.subplots()
for i in range(2010, 2021):
        plot_data=data[(data['year']==i) & (data['month']==9)]
        ax.plot(plot_data['datetime'], plot_data['flow'], '--r')

# %%
#************************************************************************
#5. scatterplot this years flow vs last years flow for Oct.
fig, ax = plt.subplots()

ax.scatter(data[(data['year'] == 2019) & (data['month'] == 10)].flow,  
data[(data['year'] == 2020) & (data['month'] == 10)].flow, marker='^',
      color='red', edgecolors='pink')
ax.set(xlabel='2019 flow', ylabel='2020 flow', yscale='log', xscale='log')
ax.legend()

# %%
#*************************************************************************

# 6. Scatter plot of flow vs day of the month for september
# Dots are colored by the year and sized acccording to the flow
sept_data = data[data['month']==9] #grabbing just september flows for plotting
fig, ax = plt.subplots()
ax.scatter(sept_data['day'], sept_data['flow'], alpha=0.2,
            s=0.02*sept_data['flow'], c=sept_data['year'], cmap='viridis')
ax.set(yscale='log')
ax.set_xlabel('Day of the month')
ax.set_ylabel('Flow')
plt.show()

#**************************************************************************
#7. Multipanel plot histograms of flow for Oct. 4-10 & Oct. 11-16
fig, ax = plt.subplots(1,2)

m = 10
month_data = data[(data['month'] == m) & (data['day'] >= 4) & (data['day'] <= 10)]
ax[0].hist(np.log10(month_data['flow']), bins=50, edgecolor='pink', color='cyan')
ax[0].set(xlim=[1.75, 2.75], xlabel='Log Flow cfs', ylabel='count', title='10/04-10 Flow')

month_data = data[(data['month'] == m) & (data['day'] >= 11) & (data['day'] <= 17)]
ax[1].hist(np.log10(month_data['flow']), bins=30,
           edgecolor='cyan', color='orange')
ax[1].set(xlabel='Log Flow cfs', ylabel='count', title='10/11-16 Flow')
plt.show()
#**************************************************************************

#8. Same as 7 but using a for loop to do all 12 months
fig, ax = plt.subplots(2, 2)
ax= ax.flatten()  #so that we can refer to plots as ax[0]...ax[3] rather than ax[0,0]..ax[1,1]
axi = 0
for m in range(9,13):
        month_data = data[data['month'] == 1]
        plot_title = 'Month ' + str(m)
        ax[axi].hist(np.log10(month_data['flow']), bins=30,
           edgecolor='grey', color='steelblue')
        ax[axi].set(xlabel='Log Flow cfs', ylabel='count', title=plot_title)
        axi=axi+1
plt.show()


#Figure out how to do multi conditionals

# %%
