# %%
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

import dataretrieval.nwis as nwis
import json
import urllib.request as req
import urllib


# %%
# Read in streamflow data for forecast from USGS website
station_id = "09506000"
start_date = '1989-01-01'
stop_date = '2021-10-23'

obs_day = nwis.get_record(sites=station_id, service='dv',
                          start=start_date, end=stop_date,
                          parameterCd='00060')

# Rename 00060_Mean column
obs_day = obs_day.rename(columns={'00060_Mean': 'flow'})

# %%
# Read in data process

mytoken = 'c36283e6b2664092979d7a1872e1b6bc'
base_url = "http://api.mesowest.net/v2/stations/timeseries"

# Specify arguments for API string
args = {
    'start': '199701010000',
    'end': '202110230000',
    'obtimezone': 'UTC',
    'vars': 'precip_accum_24_hour',
    'stids': 'KPRC',
    'units': 'temp|F,precip|mm',
    'token': mytoken}

# Connect arguments into single string
apiString = urllib.parse.urlencode(args)

# Add the API string to the base_url
fullUrl = base_url + '?' + apiString

# Generate API response
response = req.urlopen(fullUrl)

# Read the response into Python dictionary
responseDict = json.loads(response.read())

# Define variables using .keys() method to find relevant data
kprc_var = 'precip_accum_24_hour_set_1'
header = 'Precipitation'

dateTime = responseDict['STATION'][0]['OBSERVATIONS']['date_time']
precip_accum = responseDict['STATION'][0]['OBSERVATIONS'][kprc_var]

# Combine into Pandas DataFrame
data = pd.DataFrame({header: precip_accum},
                    index=pd.to_datetime(dateTime))

# Convert into weekly mean
data_weekly = data.resample('W').mean()

# %%
# Create graph to examine last three years of weekly avgs for rainfall and flow
date_form = DateFormatter("%y/%m")

fig, ax1 = plt.subplots()

ax1.plot(data_weekly.Precipitation['2019'], 'dg')
ax1.plot(data_weekly.Precipitation['2020'], 'dc')
ax1.plot(data_weekly.Precipitation['2021'], 'dy')
ax1.set(title="Observed Precipitation in Prescott, AZ\nand Flow in"
              "Verde River from 2019 to date",
        xlabel="Date", ylabel="Weekly Avg Precip in Prescott [mm]")
ax1.xaxis.set_major_formatter(date_form)

# Create a second axes that shares the same x-axis
ax2 = ax1.twinx()

ax2.plot(obs_day.flow['2019'], 'r', alpha=0.3)
ax2.plot(obs_day.flow['2020'], 'r', alpha=0.3)
ax2.plot(obs_day.flow['2021'], 'r', alpha=0.3)
ax2.set(ylabel='Verde River Weekly Flow [cfs]',
        yscale='log')
ax2.xaxis.set_major_formatter(date_form)

# Adjust frame to preserve y-labels
fig.tight_layout()

plt.grid(color='green', linestyle='--', linewidth=0.5)
plt.show()
# %%
