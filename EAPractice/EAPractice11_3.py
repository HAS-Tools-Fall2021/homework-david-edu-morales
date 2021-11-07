# %%
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# netcdf4 needs to be installed in your environment for this to work
import xarray as xr
import rioxarray
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import seaborn as sns
import geopandas as gpd
import earthpy as et

# Plotting options
sns.set(font_scale=1.3)
sns.set_style("white")

# Optional - set your working directory if you wish to use the data
# accessed lower down in this notebook (the USA state boundary data)
os.chdir(os.path.join(et.io.HOME,
                      'earth-analytics',
                      'data'))
# %%
# The (online) url for the MACAv2 data
data_path = "http://thredds.northwestknowledge.net:8080/thredds/dodsC/agg_macav2metdata_tasmax_BNU-ESM_r1i1p1_historical_1950_2005_CONUS_monthly.nc"

# Open the data using a context manager
with xr.open_dataset(data_path) as file_nc:
    # You can open the data using the code below, however it you use rio.write_crs
    # it will ensure that crs for your data persist throughout your analysis
    # max_temp_xr = file_nc
    max_temp_xr = file_nc.rio.write_crs(file_nc.rio.crs, inplace=True)

# View xarray object
max_temp_xr
# %%
# For later - grab the crs of the data using rioxarray
climate_crs = max_temp_xr.rio.crs
climate_crs
# %%
# View first 5 latitude values
max_temp_xr["air_temperature"]["lat"].values[:5]

print("The min and max latitude values in the data is:", 
      max_temp_xr["air_temperature"]["lat"].values.min(), 
      max_temp_xr["air_temperature"]["lat"].values.max())
print("The min and max longitude values in the data is:", 
      max_temp_xr["air_temperature"]["lon"].values.min(), 
      max_temp_xr["air_temperature"]["lon"].values.max())
# %%
# View first 5 and last. 5 time values - notice the span of
# dates range from 1950 to 2005
print("The earliest date in the data is:", max_temp_xr["air_temperature"]["time"].values.min())
print("The latest date in the data is:", max_temp_xr["air_temperature"]["time"].values.max()) 
# %%
max_temp_xr["air_temperature"]["time"].values.shape
# %%
# The data are lat/long (not projected)
max_temp_xr.rio.crs
# %%
# View metadata
metadata = max_temp_xr.attrs
metadata
# %%
# Above you grabbed the metadata (which is a dictionary)
# Here you can print any part of the dictionary that you wish to
metadata["title"]
# %%
key=400
longitude = max_temp_xr["air_temperature"]["lon"].values[key]
latitude = max_temp_xr["air_temperature"]["lat"].values[key]

print("Long, Lat values:", longitude, latitude)
# %%
