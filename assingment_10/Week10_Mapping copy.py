# %%
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx
import os

# %%
# Prepare data for AZ State Boundary using Geodatabase:

file = os.path.join('..', 'data',
                    'Arizona_State_Boundary-fgdb',
                    'd09edca433824603876f0a303adb5404.gdb')
fiona.listlayers(file)
azboundary = gpd.read_file(file, layer='azboundary')

# Prepare data for 2021 AZ wildfires using shapefile:
# https://azgeo-open-data-agic.hub.arcgis.com/datasets/nifc::wfigs-2021-wildland-fire-perimeters-to-date/explore?location=33.938905%2C-111.146632%2C7.92

file = os.path.join('../', 'data',
                    'WFIGS_-_2021_Wildland_Fire_Perimeters_to_Date',
                    'FH_Perimeter.shp')
fires = gpd.read_file(file)

# Select the polygon for Backbone Fire burn area:
fires_backbone = fires[fires['OBJECTID'] == 11575]

# Prepare data for AZ dams using shapefile:
# https://geodata-asu.hub.arcgis.com/datasets/asu::national-inventory-of-dams-arizona-2018/about

file = os.path.join('../', 'data',
                    'National_Inventory_of_Dams_-_Arizona_(2018)',
                    'National_Inventory_of_Dams_-_Arizona_(2018).shp')
dams = gpd.read_file(file)

# Prepare data for Ephemeral and Perennial Streams in AZ using shapefile:
# https://azgeo-open-data-agic.hub.arcgis.com/datasets/azgeo::streams-ephemeral-and-perennial/about
file = os.path.join('..', 'data',
                    'Streams___Ephemeral_and_Perennial-shp',
                    'Streams___Ephemeral_and_Perennial.shp')
streams = gpd.read_file(file)

# Pulling for large river:
verde_river = streams[streams['NAME'] == 'Verde River']
salt_river = streams[streams['NAME'] == 'Salt River']

# Prepare data for HUC1506 watershed using geodatabase:
# https://www.sciencebase.gov/catalog/item/5d30c292e4b01d82ce84aa34

file = os.path.join('..', 'data',
                    'NHDPLUS_H_1506_HU4_GDB',
                    'NHDPLUS_H_1506_HU4_GDB.gdb')
fiona.listlayers(file)
HUC8_1506 = gpd.read_file(file, layer="WBDHU8")
fires.total_bounds
dams.total_bounds

# %%
# Reproject vector objects to NAD83 | Lat(N)/Lon(E) | degrees:
azboundary_nad83 = azboundary.to_crs(HUC8_1506.crs)
fires_backbone_nad83 = fires_backbone.to_crs(HUC8_1506.crs)
dams_nad83 = dams.to_crs(HUC8_1506.crs)
verde_river_nad83 = verde_river.to_crs(HUC8_1506.crs)
salt_river_nad83 = salt_river.to_crs(HUC8_1506.crs)

# %%
dams_nad83_clip = gpd.clip(dams_nad83, HUC8_1506)

# %%
# Now look for other datasets here: 
# https://www.usgs.gov/core-science-systems/ngp/national-hydrography/access-national-hydrography-products
# https://viewer.nationalmap.gov/basic/?basemap=b1&category=nhd&title=NHD%20View

# Add some points
# UA:  32.22877495, -110.97688412
# STream gauge:  34.44833333, -111.7891667
point_list = np.array([[-110.97688412, 32.22877495],
                       [-111.7891667, 34.44833333]])
#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

#mape a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC8_1506.crs)

# %%
# plot these on the first dataset

fig, ax = plt.subplots(figsize=(10, 10))
azboundary_nad83.boundary.plot(ax=ax, color=None,
                               edgecolor='black', linewidth=1)
verde_river_nad83.plot(ax=ax,
                       linewidth=.5,
                       color='dodgerblue')
salt_river_nad83.plot(ax=ax,
                      linewidth=.5,
                      color='dodgerblue')
HUC8_1506.plot(ax=ax,
               alpha=.3,
               legend=True)
point_df.plot(ax=ax,
              color='r',
              marker='*')
dams_nad83_clip.plot(ax=ax,
                     marker='x')
fires_backbone_nad83.plot(ax=ax,
                          color='gold',
                          legend=True)
                          
ax.set_title("HUC1506 - w/ AZ Dams")
plt.show()
# %%
