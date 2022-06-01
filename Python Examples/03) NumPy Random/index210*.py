from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show()





# Difference Between Logistic and Normal Distribution
# Both distributions are near identical, but logistic distribution has more area under the tails. ie. It representage more possibility of occurence of an events further away from mean.

# For higher value of scale (standard deviation) the normal and logistic distributions are near identical apart from the peak.

# Example
