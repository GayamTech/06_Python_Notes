from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label='normal')
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label='poisson')

plt.show()




# Difference Between Normal and Poisson Distribution
# Normal distribution is continous whereas poisson is discrete.

# But we can see that similar to binomial for a large enough poisson distribution it will become similar to normal distribution with certain std dev and mean.

# Example
