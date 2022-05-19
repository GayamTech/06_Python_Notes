import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)









# Statistical Description of Data
# In order to see a summary of values in an array, we can use the describe() function.

# It returns the following description:

# number of observations (nobs)
# minimum and maximum values = minmax
# mean
# variance
# skewness
# kurtosis
# Example
# Show statistical description of the values in an array: