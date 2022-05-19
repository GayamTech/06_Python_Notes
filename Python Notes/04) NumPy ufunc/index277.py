import numpy as np

set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setxor1d(set1, set2, assume_unique=True)

print(newarr)






# Finding Symmetric Difference
# To find only the values that are NOT present in BOTH sets, use the setxor1d() method.




# Example
# Find the symmetric difference of the set1 and set2:




# Note: the setxor1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.