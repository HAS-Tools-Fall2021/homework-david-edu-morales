# %%
# Find the largest integer less than or equal to x1/x2 where x1 = all integers 1-10 & x2 =1.3:
import numpy as np

x1_array = [1,2,3,4,5,6,7,8,9,10]
div_array = np.divide(x1_array, 1.3)
div_array


# %%
#Step 1: set x1
## Different approach: x1 = np.arange(1,11)
x1 = np.array(range(1,11))  

# Step 2: set x2
x2 = 1.3

# Step 3
x3 = x1//x2
np.max(x3)

# np.floor(x1/x2)
## np.max(x3)
# %%
# Conditional Statement demonstration:
hunger = 2.9

if 8 <= hunger <= 10:
    print("Eat a meal!")
elif 3 <= hunger < 8:
      print("Eat a snack!")
else:
    print("Remember to hydrate.")

# For Loop demonstration:
hunger_list = [1,6,3,7,8,4,2,9,10]

for i in hunger_list:
    if 8 <= i <= 10:
        print("Eat a meal!")
    elif 3 <= i < 8:
        print("Eat a snack!")
    else:
        print("Remember to hydrate.")

# List comprehension 
hunger_list = [1,6,3,7,8,4,2,9,10]

new_hunger_list = [i for i in hunger_list if i >= 3]

print(np.round(np.mean(new_hunger_list), 2))


# %%
