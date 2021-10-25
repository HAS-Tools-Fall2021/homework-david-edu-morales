# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
url = "https://data.colorado.gov/resource/tv8u-hswn.json?$where=age" \
      " between 20 and 25 and year between 2020 and 2025&county=Boulder" \
      "&$select=year,age,femalepopulation"
url = url.replace(" ", "%20")
url

# %%
# Read data as JSON format
dem_data_20_25_female = pd.read_json(url)
dem_data_20_25_female.head()

# %%
# Set year as index
dem_data_20_25_female = dem_data_20_25_female.set_index("year")
dem_data_20_25_female.head()

# %%
# Pivot the data for stacked plotting
dem_data_20_25_female_pivot = dem_data_20_25_female.pivot_table('f_population',
                                                                ['year'],
                                                                "age")
dem_data_20_25_female_pivot.head()
# %%
# Plot the data
my_colors = ["teal",
             "aqua",
             "darkturquoise",
             "powderblue",
             "aliceblue",
             "lightgrey"]

f, ax = plt.subplots()
dem_data_20_25_female_pivot.plot.bar(stacked=True,
                                     color=my_colors,
                                     ax=ax).legend(loc='upper right',
                                                   bbox_to_anchor=(1.2, 1.0))
ax.set(title="Female Population in Boulder, CO by Year")

plt.show()

# %%
