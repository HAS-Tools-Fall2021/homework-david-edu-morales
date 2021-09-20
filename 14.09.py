# %%
# Data to be used:
Flow_list = [0, 1, 7, 6, 10, 24]
Day_list = [1, 6, 5, 4, 13, 11]

# List to receive output:
flow = []

# Writing list comprehension:
flow = [Flow_list[day] for day in range(len(Day_list)) \
    if Day_list[day] > 5]

print(flow)

# %%
# Methods: function attached to an object class
## Object.method(argument1) 

# Functions: tools or routines to do a specific action
## Package.funtion(arg1, arg2,...)

# Attributes: properties of an object
## Object.attribute