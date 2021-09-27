# %%
import os

import pandas as pd
import earthpy as et

# %%
# URL for .csv with avg monthly precip data
avg_monthly_precip_url = "https://ndownloader.figshare.com/files/12710618"

# Download file
et.data.get_data(url=avg_monthly_precip_url)

# %%
# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME, "earth-analytics"))

# Import data from .csv file
fname = os.path.join("data", "earthpy-downloads",
                     "avg-precip-months-seasons.csv")

avg_monthly_precip = pd.read_csv(fname)

avg_monthly_precip
# %%
# Select first row and column
avg_monthly_precip.iloc[0:1, 0:1]
# %%
# Select first two rows and first column
avg_monthly_precip.iloc[0:2, 0:1]
# %%
# Select first row and first two columns
avg_monthly_precip.iloc[0:1, 0:2]
# %%
# Select first row with all columns
avg_monthly_precip.iloc[0:1,]
# %%
# Select first column with all rows
avg_monthly_precip.iloc[:,0:1]
# %%
# Create new dataframe with 'months' as index
avg_monthly_precip_index = avg_monthly_precip.set_index("months")

avg_monthly_precip_index
# %%
avg_monthly_precip_index[["months"]]
# %%
# Select Aug using months index
avg_monthly_precip_index.loc[["Aug"]]
# %%
# Select the 'month' column as series
avg_monthly_precip["months"]
# %%
# Select the 'month' column as dataframe
avg_monthly_precip[["months"]]
# %%
# Save months and seasons to new dataframe
avg_monthly_precip_text = avg_monthly_precip[["months", "seasons"]]

avg_monthly_precip_text
# %%
# Select rows with Summer in seasons
avg_monthly_precip[avg_monthly_precip["seasons"] == "Summer"]
# %%
# Select rows with Jan in months
jan_avg_precip = avg_monthly_precip[avg_monthly_precip["months"] == "Jan"]
jan_avg_precip
# %%
# Select rows equal to 1.62 in precip
avg_monthly_precip[avg_monthly_precip["precip"] == 1.62]
# %%
# Save rows with values greater than 2.0 to new dataframe
gt2_avg_monthly_precip = avg_monthly_precip[avg_monthly_precip["precip"] > 2.0]
gt2_avg_monthly_precip
# %%
