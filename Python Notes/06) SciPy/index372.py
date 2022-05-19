import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2).pvalue

print(res)








# If you want to return only the p-value, use the pvalue property:

# Example