# %%
from matplotlib.lines import _LineStyle
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
# %%
# Using plt.figure() instance to make data container for plot data
fig = plt.figure()
ax = plt.axes()

# %%
# Using ax.plot() function to plot data into figure
fig = plt.figure()
ax = plt.axes()

x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))
# %%
# Using pylab interface to create plot
plt.plot(x, np.sin(x))
# %%
# Single figure with multiple lines
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
# %%
# Linestyle color demo
plt.plot(x, np.sin(x - 0), color='blue')        # specify color by name
plt.plot(x, np.sin(x - 1), color='g')           # short color code (rgbcmyk)
plt.plot(x, np.sin(x - 2), color='0.75')        # Grayscale between 0 and 1
plt.plot(x, np.sin(x - 3), color='#FFDD44')     # Hex code (RRGGBB from 00 to FF)
plt.plot(x, np.sin(x - 4), color=(1.0,0.2,0.3)) # RGB tuple, values 0 to 1
plt.plot(x, np.sin(x - 5), color='chartreuse'); # all HTML color names supported

# %%
# Linestyle shorthand
plt.plot(x, x + 0, lineStyle='-')
plt.plot(x, x + 1, lineStyle='--')
plt.plot(x, x + 2, lineStyle='-.')
plt.plot(x, x + 3, lineStyle=':')
# %%
# Linestyle + Color shorthand
plt.plot(x, x + 0, '-y')
plt.plot(x, x + 1, '--g')
plt.plot(x, x + 2, '-.c')
plt.plot(x, x + 3, ':r')
# %%
# Setting plot limits with plt.xlim()/ylim()
plt.plot(x, np.sin(x))

plt.xlim(-1,11)
plt.ylim(-1.5, 1.5)
# %%
# Displaying axes in reverse by swapping (-) order:
plt.plot(x, np.sin(x))

plt.xlim(10, 0)
plt.ylim(1.2, -1.2)
# %%
# Set bound limits with plt.axis() method
plt.plot(x, np.sin(x))
plt.axis([-1, 11, -1.5, 1.5])
# %%
# Tighten bounds around plot
plt.plot(x, np.sin(x))
plt.axis('tight')
# %%
# One unit x is equal to one unit y
plt.plot(x, np.sin(x))
plt.axis('equal')
# %%
# Labeling plots; titles and axis labels
plt.plot(x, np.sin(x))
plt.title("A Sine Curve")
plt.xlabel("x")
plt.ylabel("sin(x)")
# %%
# Creating plot legend using "label" keyword
plt.plot(x, np.sin(x), '-g', label='sin(x)')
plt.plot(x, np.cos(x), ':b', label='cos(x)')

plt.legend()
plt.axis('equal')
# %%
# Using object-oriented interface to plot due to differences in MATLAB-style and OO
ax = plt.axes()
ax.plot(x, np.sin(x))
ax.set(xlim=(0, 10), ylim=(-2, 2),
       xlabel='x', ylabel='sin(x)',
       title='A Simple Plot')
# %%
