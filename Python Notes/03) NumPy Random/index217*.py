from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()


# Visualization of Rayleigh Distribution
# Example



# Similarity Between Rayleigh and Chi Square Distribution
# At unit stddev the and 2 degrees of freedom rayleigh and chi square represent the same distributions.

