# %%
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
# %%
# Basic errorbar made with function
x = np.linspace(0, 10, 50)
dy = 0.8
y = np.sin(x) + dy * np.random.randn(50)

plt.errorbar(x, y, yerr=dy, fmt='.k')
# Note that fmt is format code controlling appearance of lines and points
# %%
# Formatting e-bars to make lighter than markers
plt.errorbar(x, y, yerr=dy, fmt='o', color='black',
             ecolor='lightgray', elinewidth=3, capsize=0)
# %%
