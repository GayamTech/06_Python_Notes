import numpy as np

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr)






# Finding Intersection

# To find only the values that are present in both arrays, use the intersect1d() method.






# Example
# Find intersection of the following two set arrays:




# Note: the intersect1d() method takes an optional argument assume_unique, which if set to True can speed up computation. It should always be set to True when dealing with sets.