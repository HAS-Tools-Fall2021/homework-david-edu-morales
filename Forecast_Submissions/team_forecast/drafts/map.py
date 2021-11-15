# %%
import matplotlib.pyplot as plt
import matplotlib as mpl 
import pandas as pd 
import numpy as np
import geopandas as gpd
import fiona
from shapely.geometry import Point
import contextily as ctx

# %%

file = os.path.join('..','..', 'data',"gagesII_9322_point_shapefile",
                    'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file)

type(gages)
gages.head()
gages.columns
gages.shape 

# %% 

gages.STATE.unique()
gages_AZ=gages[gages['STATE']=='AZ']
gages_AZ.shape

# Reading in a geodataframe
file = os.path.join('..','..', 'data', 'NHDPLUS_H_1506_HU4_GDB.gdb')
fiona.listlayers(file)
HUC6 = gpd.read_file(file, layer="WBDHU6")


# %%

# Add A point
# Stream gauge:  34.44833333, -111.7891667
point_list = np.array([[-111.7891667, 34.44833333]])
#make these into spatial features
point_geom = [Point(xy) for xy in point_list]
point_geom

#map a dataframe of these points
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=HUC6.crs)


# %%

# CRS = Coordinate Reference System
HUC6.crs
gages.crs

# Projecting the point
points_project = point_df.to_crs(gages_AZ.crs)


HUC6_project = HUC6.to_crs(gages_AZ.crs)

# %%
# Final Map
fig, ax = plt.subplots(figsize=(7, 10))
gages_AZ.plot(column='DRAIN_SQKM', categorical=False,
              legend=True, markersize=25, cmap='terrain',
              ax=ax)
points_project.plot(ax=ax, color='red', marker='X')
HUC6_project.boundary.plot(ax=ax, color=None,
                           edgecolor='black', linewidth=.3)
ctx.add_basemap(ax, crs=gages_AZ.crs, source = ctx.providers.OpenTopoMap)
fig.savefig("Group_Proj_Watershed")

# %%
