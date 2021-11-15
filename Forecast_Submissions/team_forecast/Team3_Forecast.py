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
from sklearn.linear_model import LinearRegression
import datetime
import dataretrieval.nwis as nwis
import os
from shapely.geometry import Point
import contextily as ctx

# %%
# Read in necessary data:
# Precipitation rate [mm/s] netCDF data from HU1506 boundaries;
# lat | 29N-40N, lon | 244E-254E
prate_path = os.path.join('..', '..', 'data',
                          'X70.164.250.222.314.12.56.9.nc')
prate = xr.open_dataset(prate_path)

# Get USGS streamflow data
station_id = "09506000"
strfdata = nwis.get_record(sites=station_id,
                           service='dv',
                           start='2000-01-01',
                           end='2021-11-08',
                           parameterCd='00060')
strfdata.columns = ['flow', 'agency_cd', 'site_no']

# Read in shapefile of gage locations for map
file = os.path.join('..', '..', 'data', "gagesII_9322_point_shapefile",
                    'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

# Reading in a geodataframe for map
file = os.path.join('..', '..', 'data', 'NHDPLUS_H_1506_HU4_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")


# %%
# Function for linear regression model estimating one/two week flows
def linreg_forecast(x, y, prate_forecast):
    """Generate 1 & 2 week streamflow forecasts using precipitation forecasts

    Parameters
    ----------
    x : numpy array
        Refers to the data associated with the linear regression model's
        indpendent variable. In this instance, the precipitation.
    y : numpy array
        Refers to the data associated with the linear regression model's
        dependent variable. In this instance, the observed stream flow.
    prate_forecast : float value
        The forecasted precipitation quantity [mm] for a location near
        the headwaters of the Verde River. Refer to any weather forecast for an
        estimated forecast value. In this instance, weather station at
        Love Field, Prescott, AZ.

    Return
    ----------
    Printed linear regression model results and one/two-week forecasts
    """
    # Build a linear regression model: y=ax+b (flow=a*prcp+b)
    model = LinearRegression()
    model.fit(x, y)

    # Results of the model
    r_sq = model.score(x, y)
    print('coefficient of determination:', np.round(r_sq, 2))

    # print the intercept and the slope
    print('intercept:', np.round(model.intercept_, 2))
    print('slope:', np.round(model.coef_, 2))

    # Prediction: precipitation input next week
    # prate_forecast = 0
    q_pred = model.intercept_ + model.coef_ * prate_forecast

    print(" This week mean flow is ", np.round(q_pred, 1))
    print(" Next week mean flow is ", np.round(q_pred, 1)-50.)

    return


# %%
# Manipulate USGS and netCDF data into numpy arrays for lin_reg function:
# Get the area averaged prate
avg_prate = prate.mean(['lat', 'lon'])

# Resample daily data into weekly mean for linear regression
wk_prate = avg_prate.to_dataframe()
wk_prate = wk_prate.resample('W').mean()

# Convert precip data, [mm/s] to [mm/day]
wk_prate['prate'] = wk_prate['prate']*3600.*24.

# Generate weekly time series for precip and streamflow during 2000-2021
W_strfdata = strfdata.resample('W').mean()

# Name objects for use in linreg_forecast function
x = wk_prate['prate'].values.reshape(-1, 1)
y = W_strfdata['flow'].values

# %%
# Generate forecast using function
linreg_forecast(x, y, 0)  # using a precip forecast value of 0 mm/day

# %% Make a timeseries plot
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(W_strfdata.index, W_strfdata.flow, color='red')

ax2 = ax.twinx()
ax2.plot(wk_prate.index, wk_prate['prate'], color='blue')
ax2.invert_yaxis()

ax.set(title="Daily Meteorology Times Series \n (09506000 VERDE RIVER NEAR \
CAMP VERDE, AZ)",  xlabel="Year", ylabel=r'Flow ($ft^3$/s)', ylim=(0, 9000))
ax2.set(ylabel='Precipitation (mm/day)', ylim=(6.5, 0))

plt.show()
fig.savefig('prcp_flow.jpg', dpi=350, bbox_inches='tight')

# %%
# Prepare map from read-in data:
# Select gages within Arizona state boundaries
gages_AZ = gages[gages['STATE'] == 'AZ']

# Added stream gauge in Camp Verde
point_list = np.array([[-111.7891667, 34.44833333]])
# Convert point into spatial feature
point_geom = [Point(xy) for xy in point_list]
# Map a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom,
                            columns=['geometry'],
                            crs=HUC6.crs)

# Reproject spatial data to NAD83
points_project = point_df.to_crs(gages_AZ.crs)
HUC6_project = HUC6.to_crs(gages_AZ.crs)

# %%
# Generate map
fig, ax = plt.subplots(figsize=(7, 10))
gages_AZ.plot(column='DRAIN_SQKM',
              categorical=False,
              legend=True,
              markersize=25,
              cmap='terrain',
              ax=ax)
points_project.plot(ax=ax,
                    color='red',
                    marker='X')
HUC6_project.boundary.plot(ax=ax,
                           color=None,
                           edgecolor='black',
                           linewidth=.3)
ctx.add_basemap(ax, crs=gages_AZ.crs,
                source=ctx.providers.OpenTopoMap)
fig.savefig("Group_Proj_Watershed")
