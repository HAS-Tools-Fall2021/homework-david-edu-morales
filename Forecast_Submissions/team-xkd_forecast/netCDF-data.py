# %%
import os

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# %%
# Read in netCDF data from HU1506 boundaries; lat | 29N-40N, lon | 244E-254E:
# Precipitation rate
datapath_prate = os.path.join('..', '..', 'data',
                              'X70.164.250.222.314.12.56.9.nc')
# Air temperature (2m)
datapath_temp = os.path.join('..', '..', 'data',
                             'X70.164.250.222.314.12.52.14.nc')

# Read in the datasets as an x-arrays
dataset_prate = xr.open_dataset(datapath_prate)
dataset_temp = xr.open_dataset(datapath_temp)

# Focusing on just the specific humidity values
prate = dataset_prate['prate']
temp = dataset_temp['air']

# Grab data for just one point
lat = dataset_prate["prate"]["lat"].values[0]
lon = dataset_prate["prate"]["lon"].values[0]
print("Long, Lat values:", lon, lat)
one_point = dataset_prate["prate"].sel(lat=lat, lon=lon)
