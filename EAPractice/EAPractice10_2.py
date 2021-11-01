# %%
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import seaborn as sns
import geopandas as gpd
from shapely.geometry import Point
import earthpy as et

# Adjust plot font sizes
sns.set(font_scale=1.5)
sns.set_style("white")

# Set a working dir & get data
data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))


# %%
# Import world boundary shapefile
worldBound_path = os.path.join("data", "spatial-vector-lidar", "global",
                               "ne_110m_land", "ne_110m_land.shp")
worldBound = gpd.read_file(worldBound_path)

# %%
# Plot worldBound data using geopandas
fig, ax = plt.subplots(figsize=(10,5))
worldBound.plot(color='darkgrey',
                ax=ax)
# Set the x an y axis labels
ax.set(xlabel="Longitude (degrees)",
       ylabel="Latitude (degrees)",
       title="Global Map - Geographic Coordinate System - WSG84 Datum\n"
             "Units: Degrees - Latitude / Longitude")                

# Add the xy graticules
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray',
              linestyle='dashed')
ax.xaxis.grid(color='gray',
              linestyle='dashed')
                          
# %%
# Create numpy array of point locations, then:
# Use floop to populate a shapely Point object
add_points = np.array([[-105.2519,   40.0274], 
                       [  10.75  ,   59.95  ], 
                       [   2.9833,   39.6167]])

# Turn points into list of xy shapely points
city_locations = [Point(xy) for xy in add_points]
city_locations

# %%
# Create geodataframe using the points
city_locations = gpd.GeoDataFrame(city_locations,
                                  columns=['geometry'],
                                  crs=worldBound.crs)
city_locations.head(3)

# %%
# Plot points on World Map
fig, ax = plt.subplots(figsize=(12, 8))

worldBound.plot(figsize=(10, 5), color='k',
                ax=ax)
# Add city locations
city_locations.plot(ax=ax,
                    color='springgreen',
                    marker='*',
                    markersize=45)

# Setup x-y axes with labels and add graticules
ax.set(xlabel="Longitude (degrees)", ylabel="Latitude (degrees)",
       title="Global Map - Geographic Coordinate System - WSG84 Datum\n"
             "Units: Degrees - Latitude / Longitutde")
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.xaxis.grid(color='gray', linestyle='dashed')

# %%
# Import graticule & world bounding box shapefile data
graticule_path = os.path.join("data", "spatial-vector-lidar", "global",
                              "ne_110m_graticules_all", "ne_110m_graticules_15.shp")
graticule = gpd.read_file(graticule_path)

bbox_path = os.path.join("data", "spatial-vector-lidar", "global", 
                         "ne_110m_graticules_all", "ne_110m_wgs84_bounding_box.shp")
bbox = gpd.read_file(bbox_path)

# Creating map axis object
fig, ax = plt.subplots(1, 1, figsize=(15, 8))

# Add bounding box and graticule layers
bbox.plot(ax=ax, alpha=.1, color='gray')
graticule.plot(ax=ax, color='lightgray')
worldBound.plot(ax=ax, color='black')

# Add points to plot
city_locations.plot(ax=ax,
                    markersize=60,
                    color='springgreen',
                    marker='*')
# Add title and axes labels
ax.set(title="World Map - Geographic Coordinate Reference System (long/lat degrees)",
       xlabel="X Coordinates (meters)",
       ylabel="Y Coordinates (meters)");       
# %%
# Reproject map using Robinson CRS
# Reproject data
worldBound_robin = worldBound.to_crs('+proj=robin')
graticule_robin = graticule.to_crs('+proj=robin')

# Plot the data
fig, ax = plt.subplots(figsize=(12, 8))

worldBound_robin.plot(ax=ax, color='k')

graticule_robin.plot(ax=ax, color='lightgray')

ax.set(title="World Map: Robinson Coordinate Reference System",
       xlabel="X Coordinates (meters)",
       ylabel="Y Coordinates (meters)")

for axis in [ax.xaxis, ax.yaxis]:
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    axis.set_major_formatter(formatter)
    
# %%
# Reproject point locations to the Robinson projection
city_locations_robin = city_locations.to_crs(worldBound_robin.crs)

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
worldBound_robin.plot(ax=ax, 
                      cmap='Greys')
ax.set(title="World map (robinson)", 
       xlabel="X Coordinates (meters)",
       ylabel="Y Coordinates (meters)")
city_locations_robin.plot(ax=ax, markersize=100, color='springgreen')

for axis in [ax.xaxis, ax.yaxis]:
    formatter = ScalarFormatter()
    formatter.set_scientific(False)
    axis.set_major_formatter(formatter)

plt.axis('equal');