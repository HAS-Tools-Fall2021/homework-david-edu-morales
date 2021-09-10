# Start code for assignment 3
# this code sets up the lists you will need for your homework
# and provides some examples of operations that will be helpful to you

# %%
# Import the modules we will use
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
# ** MODIFY **
# Set the file name and path to where you have stored the data
filename = 'streamflow_week3.txt'
filepath = os.path.join('../data', filename)
print(os.getcwd())
print(filepath)

# %%
# DON'T change this part -- this creates the lists you
# should use for the rest of the assignment
# no need to worry about how this is being done now we will cover
# this in later sections.

#Read the data into a pandas dataframe
data=pd.read_table(filepath, sep = '\t', skiprows=30,
        names=['agency_cd', 'site_no', 'datetime', 'flow', 'code']
        )

# Expand the dates to year month day
data[["year", "month", "day"]] =data["datetime"].str.split("-", expand=True)
data['year'] = data['year'].astype(int)
data['month'] = data['month'].astype(int)
data['day'] = data['day'].astype(int)

#make lists of the data
flow = data.flow.values.tolist()
date = data.datetime.values.tolist()
year = data.year.values.tolist()
month = data.month.values.tolist()
day = data.day.values.tolist()

# Getting rid of the pandas dataframe since we wont be using it this week
del(data)

# %%
# Here is some starter code to illustrate some things you might like to do
# Modify this however you would like to do your homework.
# From here on out you should use only the lists created in the last block:
# flow, date, yaer, month and day

# Calculating some basic properites
print(min(flow))
print(max(flow))
print(np.mean(flow))
print(np.std(flow))

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] > 600 and month[i] == 7:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print(len(ilist))

# ~~~ fiddling around with getting the flow value to print ~~~
print(ilist)
for j in ilist:
        print(flow [j])
# ~~~~~~

# Grabbing out the data that met the criteria
# This  subset of data is just the elements identified
# in the ilist
subset = [flow[j] for j in ilist]

# Alternatively I could have  written the for loop I used
# above to  create ilist like this
ilist2 = [i for i in range(len(flow)) if flow[i] > 600 and month[i]==7]
print(len(ilist2))

# %%
# Searching across every iteration of Sept. 13-19 since 1989 to find the average value.
sept_13_19 = []
daily_flow = []
for f in range(len(flow)):
        if month[f] == 9 and day[f] >= 13 and day[f] <= 19:
                sept_13_19.append(f)
for f_value in sept_13_19:
        daily_flow.append(flow [f_value])

y = sum(daily_flow)/len(daily_flow)
print("Avg. flow for Sept. 13-19 since 1989:", y)

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] >= y and month[i] == 9:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print("Daily flow avg has been greater than",y,len(ilist), "times.")

total_sept_days = []
for m in range(len(flow)):
        if month [m] == 9:
                total_sept_days.append(m)
perc = len(ilist)/len(total_sept_days)
print(perc*100)

pre2000 = []
for i in range(len(flow)):
        if flow [i] >= y and year [i] > 2000 and month[i] == 9:
                pre2000.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print("Daily flow avg from 1989 to 2000 has been greater than",y,len(pre2000), "times.")

total_sept_days = []
for m in range(len(flow)):
        if year [m] < 2000 and month [m] == 9:
                total_sept_days.append(m)
perc = len(pre2000)/len(total_sept_days)
print(perc*100)

# During the year 2000:
year2000 = []
for i in range(len(flow)):
        if flow [i] >= y and year [i] == 2000 and month[i] == 9:
                year2000.append(i)
print("Daily flow avg during year 2000 has been greater than",y,len(year2000), "times.")

total_sept_days = []
for m in range(len(flow)):
        if year [m] == 2000 and month [m] == 9:
                total_sept_days.append(m)
perc = len(year2000)/len(total_sept_days)
print(perc*100)

# During the year 2010:
year2010 = []
for i in range(len(flow)):
        if flow [i] >= y and year [i] == 2010 and month[i] == 9:
                year2010.append(i)
print("Daily flow avg during year 2010 has been greater than",y,len(year2010), "times.")

total_sept_days = []
for m in range(len(flow)):
        if year [m] == 2010 and month [m] == 9:
                total_sept_days.append(m)
perc = len(year2010)/len(total_sept_days)
print(perc*100)

# After the year 2010:
post2010 = []
for i in range(len(flow)):
        if flow [i] >= y and year [i] > 2010 and month[i] == 9:
                post2010.append(i)
print("Daily flow avg after year 2010 has been greater than",y,len(post2010), "times.")

total_sept_days = []
for m in range(len(flow)):
        if year [m] > 2010 and month [m] == 9:
                total_sept_days.append(m)
perc = len(post2010)/len(total_sept_days)
print(perc*100)

# %%
# Searching across every iteration of Sept. 20-26 since 1989 to find the average value.
sept_20_26 = []
daily_flow = []
for f in range(len(flow)):
        if month[f] == 9 and day[f] >= 20 and day[f] <= 26:
                sept_20_26.append(f)
for f_value in sept_20_26:
        daily_flow.append(flow [f_value])

z = sum(daily_flow)/len(daily_flow)
print("Avg. flow for Sept. 20-26 since 1989:", z)

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] >= z and month[i] == 9:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print("Daily flow avg has been greater than",z,len(ilist), "times.")

total_sept_days = []
for m in range(len(flow)):
        if month [m] == 9:
                total_sept_days.append(m)
perc = len(ilist)/len(total_sept_days)
print(perc*100)

# %%
#Finding flow average for 1st half of Sept. since 1989:
sept_first_half = []
daily_flow = []
for f in range(len(flow)):
        if month[f] == 9 and day[f] >= 1 and day[f] <= 15:
                sept_first_half.append(f)
for f_value in sept_first_half:
        daily_flow.append(flow [f_value])

z = sum(daily_flow)/len(daily_flow)
print("Avg. flow for first half of Sept. since 1989:", z)
# %%
#Finding flow average for 2nd half of Sept. since 1989:
sept_second_half = []
daily_flow = []
for f in range(len(flow)):
        if month[f] == 9 and day[f] >= 16 and day[f] <= 30:
                sept_second_half.append(f)
for f_value in sept_second_half:
        daily_flow.append(flow [f_value])

z = sum(daily_flow)/len(daily_flow)
print("Avg. flow for second half of Sept. since 1989:", z)

# %%
# %%
# Evaluating how many times daily avg flow surpassed prediciton in years prior to 2000:
sept_13_19 = []
daily_flow = []
for f in range(len(flow)):
        if month[f] == 9 and day[f] >= 13 and day[f] <= 19:
                sept_13_19.append(f)
for f_value in sept_13_19:
        daily_flow.append(flow [f_value])

y = sum(daily_flow)/len(daily_flow)
print("Avg. flow for Sept. 13-19 since 1989:", y)

# Making and empty list that I will use to store
# index values I'm interested in
ilist = []

# Loop over the length of the flow list
# and adding the index value to the ilist
# if it meets some criteria that I specify
for i in range(len(flow)):
        if flow [i] >= y and year [i] > 2000 and month[i] == 9:
                ilist.append(i)

# see how many times the criteria was met by checking the length
# of the index list that was generated
print("Daily flow avg from 1989 to 2000 has been greater than",y,len(ilist), "times.")

total_sept_days = []
for m in range(len(flow)):
        if year [m] < 2000 and month [m] == 9:
                total_sept_days.append(m)
perc = len(ilist)/len(total_sept_days)
print(perc*100)


# %%
