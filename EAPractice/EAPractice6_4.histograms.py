# %%
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

data = np.random.randn(1000)
# %%
# Plot histogram of data
plt.hist(data)
# %%
# Futher customize histogram
plt.hist(data, bins=30, normed=True, alpha=0.5,
         histtype='stepfilled', color='steelblue',
         edgecolor='none')
# %%
# Stepfilled and transparency useful when comparing hists
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
# %%
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)

kwargs = dict(histtype='stepfilled', alpha=0.3, normed=True, bins=40)

plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
# %%
# In order to compute the hist w/o displaying:
counts, bin_edges = np.histogram(data, bins=5)
print(counts)
# %%
# 2-dimensional histogram data(defining data drawn from
# Gaussian distribution)
mean = [0, 0]
cov = [[1,1], [1,2]]
x, y = np.random.multivariate_normal(mean, cov, 10000).T
# %%
# Plotting 2D histogram
plt.hist2d(x, y, bins=30, cmap='Blues')
cb = plt.colorbar()
cb.set_label('counts in bin')
# %%
# 2D Hist with hexagonal binning
plt.hexbin(x, y, gridsize=30, cmap='Blues')
cb = plt.colorbar(label='count in bin')
# %%
