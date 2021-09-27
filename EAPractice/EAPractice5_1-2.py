# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%
# Average monthly precip for Boulder, CO
avg_monthly_precip = pd.DataFrame(columns=["month", "precip_in"],
                                  data=[
                                      ["Jan", 0.70], ["Feb", 0.75],
                                      ["Mar", 1.85], ["Apr", 2.93],
                                      ["May", 3.05], ["June", 2.02],
                                      ["July", 1.93], ["Aug", 1.62],
                                      ["Sept", 1.84], ["Oct", 1.31],
                                      ["Nov", 1.39], ["Dec", 0.84]
])
# %%
f, ax = plt.subplots()
avg_monthly_precip.plot(x="month",
                        y="precip_in",
                        title="Plot of Pandas data Frame using Pandas .plot",
                        ax=ax)
plt.show()
# %%
f, ax = plt.subplots()
ax.plot(avg_monthly_precip.month,
        avg_monthly_precip.precip_in)

ax.set(title="Plot of Pandas Data Frame using Pandas .plot")
plt.show(   )

# %%
import os

import matplotlib.pyplot as plt
import pandas as pd
import earthpy as et

# %%
# URL for .csv with avg monthly precip data
avg_monthly_precip_url = "https://ndownloader.figshare.com/files/12710618"

# Download file from URL
et.data.get_data(url=avg_monthly_precip_url)

# %%
# Set working directory to earth-analytics
os.chdir(os.path.join(et.io.HOME,
                      "earth-analytics",
                      "data"))
# %%
# Import data from .csv file
fname = os.path.join("earthpy-downloads",
                     "avg-precip-months-seasons.csv")

avg_monthly_precip = pd.read_csv(fname)

avg_monthly_precip
# %%
# Create a bar graph of using the Pandas DataFrame
f, ax = plt.subplots()
ax.bar(x=avg_monthly_precip.months,
       height=avg_monthly_precip.precip)

ax.set(title="Plot of Pandas Data Frame using Pandas .plot")
plt.show()

# %%
# Creating a line graph of the same data
f, ax = plt.subplots()
ax.plot(avg_monthly_precip.months,
        avg_monthly_precip.precip)

ax.set(title="Plot of Pandas Data Frame using Pandas")
plt.show()
# %%
