import os

from pkg_resources import fixup_namespace_packages

# %%
my_path = os.path.join("Desert Varnish", "Users", "moral", "Documents")

os.path.exists(my_path)
# %%
os.getcwd()
# %%
os.chdir("HAS_Tools")
# %%
os.chdir(os.path.join("C:", "Users", "moral", "HAS_Tools"))
# %%
os.getcwd( )
# %%
os.chdir('HAS_Tools\\homework-david-edu-morales')
# %%
os.chdir('c:\\Users\\moral\\HAS_Tools')
# %%
os.getcwd()
# %%
import numpy as np
# %%
# Monthly avg precip forr Jan through Mar in Boulder, CO
avg_monthly_precip = np.array([0.7, 0.75, 1.85])

print(avg_monthly_precip)

# Monthly preicp for Jan through Mar in 2002 and 2013
precip_2002_2013 = np.array([
    [1.07, 0.44, 1.50],
    [0.27, 1.13, 1.72]
])

print(precip_2002_2013)


# %%
import earthpy as et
# %%
# Download .txt with avg monthly precip (inches)
monthly_precip_url = 'https://ndownloader.figshare.com/files/12565616'
et.data.get_data(url=monthly_precip_url)

# Download .csv of precip data for 2002 and 2013 (inches)
precip_2002_2013_url = 'https://ndownloader.figshare.com/files/12707792'
et.data.get_data(url=precip_2002_2013_url)

# %%
# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME, 'earth-analytics'))
# %%
# Import average monthly precip to numpy array
fname = os.path.join("data", "earthpy-downloads", "avg-monthly-precip.txt")

avg_monthly_precip = np.loadtxt(fname)

print(avg_monthly_precip)
# %%
# Import monthly precip for 2002 and 2013 to numpy array
fname = os.path.join("data", "earthpy-downloads", "monthly-precip-2002-2013.csv")

precip_2002_2013 = np.loadtxt(fname, delimiter = ",")

print(precip_2002_2013)
# %%
avg_monthly_precip.ndim
# %%
precip_2002_2013.ndim
# %%
precip_2002_2013.shape
avg_monthly_precip.shape
# %%
avg_monthly_precip_mm = avg_monthly_precip * 25.4
# %%
print(avg_monthly_precip)
# %%
# Use assignment operator to convert values from into mm
avg_monthly_precip *= 25.4

# Print new values
print(avg_monthly_precip)

# %%
# Check original values
print(precip_2002_2013)
# %%
# Use assignment operator to convert values from in to mm
precip_2002_2013 *= 25.4

# Print new values
print(precip_2002_2013)

# %%
precip_list = [.7, 0.75, 1.85, 2.93, 3.05, 2.02, 1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

precip_list *= 25.4

# %%
precip_list_mm = [i * 25.4 for i in precip_list]
print(precip_list_mm)

# %%
# Create variable with mean value
mean_avg_precip = np.mean(avg_monthly_precip)

print("mean average monthly precipitation:", mean_avg_precip)
# %%
# Create varaible with median value
median_avg_precip = np.median(avg_monthly_precip)

print(median_avg_precip)
# %%
np.std(avg_monthly_precip)
# %%
# Calculate and print minimum and maximum values
print("min avg monthly precip:", np.min(avg_monthly_precip))
print("max avg monthly precip", np.max(avg_monthly_precip))
# %%
# Visually identify max value across the rows of precip_2002_2013
print(precip_2002_2013)
# %%
print(np.max(precip_2002_2013, axis = 0))
# %%
# Create new array of the max value for each month
precip_2002_2013_monthly_max = np.max(precip_2002_2013, axis = 0)

type(precip_2002_2013_monthly_max)
# %%
# Maximum value for each year 2002 and 2013
print(np.max(precip_2002_2013, axis = 1))
# %%
# Check shape
avg_monthly_precip.shape
# %%
# Select the last element of 12 elements
avg_monthly_precip[12]
# %%
avg_monthly_precip[-1]
# %%
# Slice range from 3rd to 5th elements
print(avg_monthly_precip[2:5])
# %%
# Check shape
precip_2002_2013.shape
# %%
# Select element in 2nd row, 3rd column
precip_2002_2013[1,2]
# %%
# Select element in 2nd row, 12th column
precip_2002_2013[1,11]
# %%
# Slice first row, first two columns
precip_2002_2013[0:1,0:2]
# %%
precip_2002_2013[0:,0:1]
# %%
# Slice first two rows, first two columns
precip_2002_2013[:2,:2]
# %%
precip_2002_2013[:,0]
# %%
# Select 1st row of data for 2002
precip_2002 = precip_2002_2013[0,:]

print(precip_2002.shape)
print(precip_2002)
# %%
# Select 2nd row of data for 2013
precip_2013 = precip_2002_2013[1]

print(precip_2013.shape)
print(precip_2013)
# %%
