from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=1000, p=0.01, size=1000), hist=False, label='binomial')
sns.distplot(random.poisson(lam=10, size=1000), hist=False, label='poisson')

plt.show()




# Difference Between Poisson and Binomial Distribution

# The difference is very subtle it is that, binomial distribution is for discrete trials, whereas poisson distribution is for continuous trials.

# But for very large n and near-zero p binomial distribution is near identical to poisson distribution such that n * p is nearly equal to lam.

# Example
