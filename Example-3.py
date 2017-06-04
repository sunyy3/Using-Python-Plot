# Example 3: how to plot histogram from raw data

import matplotlib.pyplot as plt
import random
import numpy as np

Alist = []
for i in range(300):
    Alist.append(random.randint(1, 100))

# First, plot histogram using count number in every bin range
# Define 20 bins from 0 to 100, every 5 as one bin, Note: right boundary
# doesn't include.
bins = np.arange(0, 105, 5)

plt.clf()
plt.hist(Alist, bins=bins, alpha=0.5, color='red', edgecolor='black')
# option: 'edgecolor' define outline color
plt.ylabel('count')
plt.show()

# Second, we can also plot normalized histgram using probability of every bin
# Note: the option: "normed=True" won't give us correct figure, here we
# need using "weights"
# Basically, here "weights" does: instead of counting every data point in
# "Alist" as 1, it count as 1/len(Alist), then we easily get the probability
weight_Alist = np.ones_like(Alist) / len(Alist)
bins = np.arange(0, 105, 5)
plt.clf()
plt.hist(Alist, bins=bins, alpha=0.5, color='red', edgecolor='black',
    weights=weight_Alist)
plt.ylabel('Probability')
plt.show()

# Third, if you want to know exactly value of each bins, we can using "numpy"
bins = np.arange(0, 105, 5)
histRes, bin_width = np.histogram(Alist, bins)
# NOTE: the length of bin_width is larger than the length of histRes by 1.
print(histRes, len(histRes))
print(bin_width, len(bin_width))