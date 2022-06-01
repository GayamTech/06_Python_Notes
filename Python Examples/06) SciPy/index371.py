import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)















# SciPy Statistical Significance Tests
# What is Statistical Significance Test?
# In statistics, statistical significance means that the result that was produced has a reason behind it, it was not produced randomly, or by chance.

# SciPy provides us with a module called scipy.stats, which has functions for performing statistical significance tests.

# Here are some techniques and keywords that are important when performing such tests:

# Hypothesis in Statistics
# Hypothesis is an assumption about a parameter in population.

# Null Hypothesis
# It assumes that the observation is not statistically significant.

# Alternate Hypothesis
# It assumes that the observations are due to some reason.

# Its alternate to Null Hypothesis.

# Example:

# For an assessment of a student we would take:

# "student is worse than average" - as a null hypothesis, and:

# "student is better than average" - as an alternate hypothesis.

# One tailed test
# When our hypothesis is testing for one side of the value only, it is called "one tailed test".

# Example:

# For the null hypothesis:

# "the mean is equal to k", we can have alternate hypothesis:

# "the mean is less than k", or:

# "the mean is greater than k"

# Two tailed test
# When our hypothesis is testing for both side of the values.

# Example:

# For the null hypothesis:

# "the mean is equal to k", we can have alternate hypothesis:

# "the mean is not equal to k"

# In this case the mean is less than, or greater than k, and both sides are to be checked.

# Alpha value
# Alpha value is the level of significance.

# Example:

# How close to extremes the data must be for null hypothesis to be rejected.

# It is usually taken as 0.01, 0.05, or 0.1.

# P value
# P value tells how close to extreme the data actually is.

# P value and alpha values are compared to establish the statistical significance.

# If p value <= alpha we reject the null hypothesis and say that the data is statistically significant. otherwise we accept the null hypothesis.

















# T-Test
# T-tests are used to determine if there is significant deference between means of two variables. and lets us know if they belong to the same distribution.

# It is a two tailed test.

# The function ttest_ind() takes two samples of same size and produces a tuple of t-statistic and p-value.








# Example
# Find if the given values v1 and v2 are from same distribution: