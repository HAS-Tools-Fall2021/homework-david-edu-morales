# %%
import os
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
# %%
# Using plt.plot and ax.plot to make scatter plots
x = np.linspace(0, 10, 30)
y = np.sin(x)

plt.plot(x, y, 'o', color='black')
# %%
# Demonstrate use of different plot symbols
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
    label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)
# %%
# Stringing together marker code into linestyle shorthand
plt.plot(x,y, '-ok')
# %%
# Adding keyword arguments to specify different properties
plt.plot(x, y, '-p', color='red',
         markersize=15, linewidth=4,
         markerfacecolor='cyan',
         markeredgecolor='yellow',
         markeredgewidth=2)
plt.ylim(-1.2, 1.2)
# %%
# More powerful method of creating scatterplots
plt.scatter(x, y, marker='o')
# %%
# plt.scatter allows for different marker properties can be individually controlled
    # or mapped to data.
rng = np.random.RandomState(0)
x = rng.randn(100)
y = rng.randn(100)
colors = rng.rand(100)
sizes = 1000 * rng.rand(100)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.3,
            cmap='viridis')
plt.colorbar()
# %%
