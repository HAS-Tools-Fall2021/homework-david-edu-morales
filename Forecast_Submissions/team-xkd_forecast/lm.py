# %%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import fiona
import shapely
from netCDF4 import Dataset
from   sklearn.linear_model import LinearRegression
import datetime
import dataretrieval.nwis as nwis
# %%
# Read in netCDF data from HU1506 boundaries; lat | 29N-40N, lon | 244E-254E:
# Precipitation rate (mm/s)
prate_path = os.path.join('..', '..', 'data',
                              'X70.164.250.222.314.12.56.9.nc')
prate = xr.open_dataset(prate_path)
 
prate

# Get the area averaged prate
avg_prate = prate.mean(['lat', 'lon'])

# Resample daily data into weekly mean for linear regression
wk_prate = avg_prate.to_dataframe()
wk_prate = wk_prate.resample('W').mean()
wk_prate['prate'] = wk_prate['prate']*3600.*24.

# Get USGS streamflow data
station_id = "09506000"
strfdata = nwis.get_record(sites=station_id, service='dv', start='2000-01-01', end='2021-11-08', parameterCd='00060')
strfdata.columns = ['flow', 'agency_cd', 'site_no']

# Generate weekly time series for prcp and streamflow during 1989-2020
W_strfdata = strfdata.resample('W').mean()

# %%
# Build a linear regression model: y=ax+b (flow=a*prcp+b) 
model = LinearRegression()
x = wk_prate['prate'].values.reshape(-1, 1)
y = W_strfdata['flow'].values
model.fit(x, y)

# Results of the model
r_sq = model.score(x, y)
print('coefficient of determination:', np.round(r_sq, 2))

# print the intercept and the slope
print('intercept:', np.round(model.intercept_, 2))
print('slope:', np.round(model.coef_, 2))

# Prediction: precipitation input next week
prate_forecast = 0.1
q_pred = model.intercept_ + model.coef_ * prate_forecast

print(" This week mean flow is ", np.round(q_pred, 1))
print(" Next week mean flow is ", np.round(q_pred, 1)-50.)

# %% Make a timeseries plot
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(W_strfdata.index, W_strfdata.flow, color='red')

ax2 = ax.twinx()
ax2.plot(wk_prate.index, wk_prate['prate'], color='blue')
ax2.invert_yaxis()

ax.set(title="Daily Meteorology Times Series \n (09506000 VERDE RIVER NEAR \
CAMP VERDE, AZ",  xlabel="Year", ylabel=r'Flow ($ft^3$/s)', ylim=(0, 9000))
ax2.set(ylabel='Precipitation (mm/day)', ylim=(6.5, 0))

plt.show()
fig.savefig('prcp_flow.jpg', dpi=350, bbox_inches='tight')

# %%
