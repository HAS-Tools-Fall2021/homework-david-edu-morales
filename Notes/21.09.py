# %%
# WARM UP
import numpy as np

# Make a matrix of random numbers:
array = np.random.randn(6,12)

## array = np.random.randomint(1, 100, (6, 12))

# Find statistical values
print("Array avg. valuge:", np.round(np.mean(array), 2))
print("Array standard deviaiton:", np.round(np.std(array), 2))
print("Avg. value for 3rd column:", np.round(np.mean(array[:,2]), 2))

# Find stat values of (a) every row and (b) every column:
# (a) avg of every row
row_avg = np.round(np.mean(array, axis=1), 2)
print(row_avg)

# (b) avg of every column
column_avg = np.round(np.mean(array, axis=0), 2)
print(column_avg)

