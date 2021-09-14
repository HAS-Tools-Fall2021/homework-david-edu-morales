# %%
tucson_precip_in=[0.7,0.75,1.85]
tucson_precip_in.insert(2,1.0)
tucson_precip_in[0:3]
months=["January","February","March","April","May","June","July"]
months[1]
type(tucson_precip_in)
len(tucson_precip_in)
len(months)
print("The lengh of the months list is:", len(months))
tucson_precip_in[0]=0.68
tucson_precip_in
months.insert(7,"August")
months
del months[7]
tucson_precip_in.append(3.2)
# %%
list_of_lists=[[1,2,3],[8,9,10]]
list_of_lists
# %%
list_of_lists[0]
type(list_of_lists[0])
# %%
list_of_lists[1][2]
# %%
a=1
b=2
a+b
# %%
b-a
b/a
b*a
a**b
b**a
# %%
jan_precip_in=.7
inches_to_mm=25.4
jan_precip_in*inches_to_mm

# %%
march_precip_in=1.5
march_precip_mm = march_precip_in*inches_to_mm
march_precip_mm
type(march_precip_mm)
# %%
march_precip_in
# %%
march_precip_in*=inches_to_mm
march_precip_in
# %%
march_precip_in

# %%
annual_avg_precip_nyc=42.65
dec_avg_precip_nyc=3.58
annual_avg_precip_nyc+=dec_avg_precip_nyc
annual_avg_precip_nyc
# %%
print(a,b,annual_avg_precip_nyc)
# %%
print("Annual Preciption in NYC (inches):",annual_avg_precip_nyc)

# %%
temp=[60,70,80]
60 in temp
# %%
60 in temp and 70 in temp
# %%
65 in temp
# %%
id(a)
# %%
temp_1=[70,68,74]
temp_2=[70,68,74]
temp_3=temp_1

# %%
temp_1 is temp_3
# %%
temp_1==temp_2
# %%
temp_1 is temp_2
# %%
temp_1 is not temp_2
# %%
boulder_precip_months=["jan","feb","mar","apr","may","june","july","aug","sept","oct","nov","dec"]
boulder_precip_inches=[0.7,0.75,1.85,2.93,3.05,2.02,1.93,1.62,1.84,1.31,1.39,0.84]
type(boulder_precip_inches)
type(boulder_precip_months)
# %%
x=0
if x== 10:
    print("x is equal to 10")
else:
    print("x has a value of", x, "which is not equal to 10")

# %%
x = 10
if x < 10:
    print("x has a value of", x, "which is less than 10")
else:
    print("x has a value of", x, "which is greater than 10")

# %%
y = -10
if x > y:
    print("x has a value of", x, "which is greater than", y)
else:
    print("x has a value of", x, "which is less than", y)

# %%
y = 100
if x > y:
    print("x has a value of", x, "which is greater than", y)
else:
    print("x has a value of", x, "which is less than", y)

# %%
avg_monthly_precip = [0.7,0.75,1.85,2.93,3.05,2.02,1.93,1.62,1.84,1.31,1.39,0.84]
if 0.70 in avg_monthly_precip:
    print("value is in list")
else:
    print("value is not in list")
# %%
if 0.71 in avg_monthly_precip:
    print("value is in list")
else:
    print("value is not in list")
# %%
x=0
if type(x) is int:
    print(x, "is an integer.")
else:
    print(x, "is not an integer")

# %%
0.71*2
# %%
if type(x) is float:
    print(x, "is a float.")
else:
    print(x, "is not a float.")
# %%
if type(x) is not str:
    print(x, "is not a string.")
else:
    print(x, "is a string.")
# %%
months = ["Jan","Feb","Mar","Apr","June","July","Aug","Sept","Oct","Nov","Dec"]
if type(months) is list:
    print("Object is a list.")
else:
    print("Object is not a list.")
# %%
if type(avg_monthly_precip) is type(months):
    print("These objects are of the same type.")
else:
    print("These objects are not of the same type.")
# %%
import os
import numpy as np
import earthpy as et
# %%
import earthpy as et

# %%
for x in range(4):
    print(x)
print("done")
# %%
mylist=[0,5,7,9]
for x in mylist:
    print(x)
    if x>5:
        print("Large")
print("done")
# %%
mylist=["a","b","c","d"]
pick=[1,0,3]
newlist=[]
for i in pick:
    print(mylist[i])
    newlist.append(mylist[i])
print(newlist)
# %%
mylist=["a","b","c","d"]
pick=[1,0,3]
newlist=[mylist[i] for i in pick]
# This is called a list comprehension

# %%
x = 5
y = 10

if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is already equal to y.")

else:
    print("x started wit ha value of", x, "which is already equal to y.")
    # %%
x = 15

if x < y:
    print("x started with value of", x)
    x+= 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x,"which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")

# %%
x = 10

if x < y:
    print("x started with value of", x)
    x += 5
    print("It now has a value of", x, "which is equal to y.")

elif x > y:
    print("x started with value of", x)
    x -= 5
    print("It now has a value of", x, "which is equal to y.")

else:
    print("x started with a value of", x, "which is already equal to y.")

# %%
if "precip" in "avg_monthly_temp":
    fname = "avg_monthly_temp"
    print(fname)

elif "precip" in "avg_monthly_precip":
    fname = "avg_monthly_precip"
    print(fname)

else:
    print("Neither textstring contains the word precip.")

# %%
avg_monthly_precip = [0.70, 0.75, 1.85, 2.93, 3.05, 2.02, 1.93, 1.62, 1.84, 1.31, 1.39]

if avg_monthly_precip[-1] == 0.84:
    print(avg_monthly_precip[-1])
    
elif avg_monthly_precip[-1] == 1.39:
    avg_monthly_precip += [0.84]
    print(avg_monthly_precip)

else:
    print("The last item in the list is neither 0.84 nor 1.39")

# %%
x = 5
y = 10

if type(x) is int and type(y) is int:
    print(x +y)

else:
    print("Either x or y is not an integer.")

# %%
x = 5
y = "some text"

if type(x) is int and type(y) is int:
    print(x + y)

else:
    print("Either x or y is not an integer, so they cannot be added.")

# %%
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov"]

precip_len = len(avg_monthly_precip)
print(precip_len)

months_len = len(months)
print(months_len)

# %%
if type(avg_monthly_precip) is type(months) and precip_len == months_len:
    print("Objects are of the same type and have the same length.")
else:
    print("Objects are not of the same type or do not have same length.")


# %%
x = 0
y = 10

if x == 0 or y == 0:
    print("Either x or y is equal to 0.")
    x += 1
    y += 1
    print("x is now", x, "and y is now", y)

else:
    print("Neither x nor y is equal to 0.")


# %%
if type(avg_monthly_precip) is type(months) or precip_len == months_len:
    print("Objects have either the same type or length.")
else:
    print("Objects either do not have the same type or same length.")
# %%
list_of_values = [1,2,3,4,5]

print(list_of_values)
# %%
for avalue in list_of_values:
    print(avalue)
# %%
for avalue in list_of_values:
    print("the current value is:", avalue)

# %%
num_list = [12, 5, 136, 47]

for i in num_list:
    i += 10
    print(i)

# %%
num_list = [12, 5, 136, 47]

for x in num_list:
    x += 10
    print("The value of the variable 'x' is:", x)
# %%
num_list = [12, 5, 136, 47]

for banana in num_list:
    banana += 10
    print("The value of the variable 'banana' is:", banana)

# %%
files = ["months.txt", "avg-monthly-precip.txt"]

for fname in files:
    print("The value of the variable 'fname' is:", fname)

# %%
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

avg_monthly_precip = [0.70, 0.75, 1.85, 2.93, 3.05, 2.02, 1.93, 1.62, 1.84, 1.31, 1.39, 0.84]

lists = [months, avg_monthly_precip]

for dlist in lists:
    print("the value of the variable 'dlist' is:", dlist)

# %%
for dlist in lists:
    print("The length of the variable 'dlist' is:", len(dlist))
# %%
for dlist in lists:
    print(dlist[-1])

# %%
for dlist in lists:
    print(dlist.shape)
# %%
%%time
for_list = []
for i in range(50000):
    for_list.append(i*i)

# %%
%%time
comp_list = [i*i for i in range(50000)]

# %%
[month * 25.4 for month in avg_monthly_precip]
# %%
def convert_in_to_mm(num):
    return num * 25.4

[convert_in_to_mm(month) for month in avg_monthly_precip]
# %%
[month for month in avg_monthly_precip if month > 1.5]

# %%
[month * -2 if month > 1.5 else month * 2 for month in avg_monthly_precip]
# %%
