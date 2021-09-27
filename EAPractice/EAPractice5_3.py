# %%
import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et

# %%
# URL for .csv with avg monthly precip data
avg_monthly_precip_url = "https://ndownloader.figshare.com/files/12710618"

# Download file
et.data.get_data(url=avg_monthly_precip_url)


# %%
# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME,
                      "earth-analytics",
                      "data"))
# Import data from .csv file
fname = os.path.join("earthpy-downloads",
                     "avg-precip-months-seasons.csv")

avg_monthly_precip = pd.read_csv(fname)

avg_monthly_precip
# %%
# See first 5 rows
avg_monthly_precip.head()
# %%
# See last 5 rows
avg_monthly_precip.tail()
# %%
# Information about the dataframe
avg_monthly_precip.info()
# %%
# Get column names
avg_monthly_precip.columns
# %%
# Number of rows and columns
avg_monthly_precip.shape
# %%
# Summary stats of all numeric columns
avg_monthly_precip.describe()
# %%
# Median of all numeric columns
avg_monthly_precip.median()
# %%
# Summary stats on precip column as dataframe
avg_monthly_precip[["precip"]].describe()
# %%
# Summary stats on precip column  as series
avg_monthly_precip["precip"].describe()
# %%
# Sort in descending order for precip
avg_monthly_precip.sort_values(by="precip",
                               ascending=False)
# %%
# Convert values from inches to millimeters
avg_monthly_precip["precip"] *= 25.4

avg_monthly_precip
# %%
# Create new column wit hprecip in the original unites (inches)
avg_monthly_precip["precip_in"] = avg_monthly_precip["precip"] / 25.4

avg_monthly_precip
# %%
# Plot the data
f, ax = plt.subplots()

ax.bar(x=avg_monthly_precip.months,
       height=avg_monthly_precip.precip,
       color="purple")
ax.set(title="Plot of Average Monthly Precipitation in mm")
plt.show()
# %%
# Group data by seasons and summarize precip
precip_by_season=avg_monthly_precip.groupby(["seasons"])[["precip"]].describe()
precip_by_season
# %%
precip_by_season.columns
# %%
# Drop a level so there is only one index
precip_by_season.columns = precip_by_season.columns.droplevel(0)
precip_by_season
# %%
# Plot the data
f, ax = plt.subplots()

ax.bar(precip_by_season.index,
       precip_by_season["mean"],
       color="purple")

ax.set(title="Bar Plot of Seasonal Monthly Precipitation in mm")       
plt.show()
# %%
# Save median of precip for each season to dataframe
avg_monthly_precip_median = avg_monthly_precip.groupby(
    ["seasons"])[["precip"]].median()

avg_monthly_precip_median
# %%
# Save to new dataframe with original index
avg_monthly_precip_median = avg_monthly_precip.groupby(
    ["seasons"], as_index=False)[["precip"]].median()

avg_monthly_precip_median
# %%
# Save summary stats of precip for each season to dataframe
avg_monthly_precip_stats = avg_monthly_precip.groupby(
    ["seasons"])[["precip"]].describe()

avg_monthly_precip_stats
# %%
# Reset index
avg_monthly_precip_stats.reset_index(inplace=True)

avg_monthly_precip_stats
# %%
