# %%
import os
import matplotlib.pyplot as plt
import geopandas as gpd
import earthpy as et

# %%
# Get data and set working directory
data = et.data.get_data('spatial-vector-lidar')
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))

# %%
# Define path to file
plot_centroid_path = os.path.join("data", "spatial-vector-lidar",
                                  "california", "neon-sjer-site",
                                  "vector_data", "SJER_plot_centroids.shp")

# Import shapefile using geopandas
sjer_plot_locations = gpd.read_file(plot_centroid_path)

# %%
# View the geometry type of each row
sjer_plot_locations.geom_type

# %%
# View object type
type(sjer_plot_locations)

# %%
# View CRS of object
sjer_plot_locations.crs

# %%
# View the spatial extent
sjer_plot_locations.total_bounds

# %%
# View number of features (rows, columns)
sjer_plot_locations.shape

# %%
sjer_plot_locations.plot()

# %%
fig, ax1 = plt.subplots(figsize = (10, 10))

# Plot the data using geopandas .plot() method
sjer_plot_locations.plot(ax=ax1)

plt.show()

# %%
fig, ax = plt.subplots(figsize = (10, 10))

# Plot the data and add a legend
sjer_plot_locations.plot(column='plot_type',
                         categorical=True,
                         legend=True,
                         figsize=(10, 6),
                         markersize=45,
                         cmap="Set2",
                         ax=ax)
# Add a title
ax.set_title("SJER Plot Locations\nMadera County, CA")

plt.show()

# %%
# Fiddling with different styles
fig, ax = plt.subplots(figsize = (10, 10))

# Plot the data and add a legend
sjer_plot_locations.plot(column='plot_type',
                         categorical=True,
                         legend=True,
                         marker='*',
                         markersize=65,
                         cmap="OrRd",
                         ax=ax)
# Add a title
ax.set_title("SJER Plot Locations\nMadera County, CA")

plt.show()
# %%
# Prepare to plot multiple shapefiles together
# Define path to crop boundary
sjer_crop_extent_path = os.path.join("data", "spatial-vector-lidar",
                                     "california", "neon-sjer-site",
                                     "vector_data", "SJER_crop.shp")
# Import crop boundary
sjer_crop_extent = gpd.read_file(sjer_crop_extent_path)

# %%
# Plot multiple shapefiles together
fig, ax = plt.subplots(figsize=(10, 10))

# First setup the plot using the crop_extent layer as the base layer
sjer_crop_extent.plot(color='lightgray',
                      edgecolor='black',
                      alpha=.5,
                      ax=ax)

# Add  another layer using the same ax
sjer_plot_locations.plot(column='plot_type',
                         categorical=True,
                         marker='*',
                         legend=True,
                         markersize=50,
                         cmap='Set2', ax=ax)
# Clean up axes
ax.set_title('SJER Plot Locations\nMadera County, CA')
ax.set_axis_off() # used to turn off the x and y axis

plt.axis('equal') # used to ensure the x and y axis are uniformly spaced
plt.show()
# %%
