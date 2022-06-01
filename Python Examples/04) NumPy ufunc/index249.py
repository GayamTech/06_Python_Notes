import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2], axis=1)

print(newarr)




# Summation Over an Axis
# If you specify axis=1, NumPy will sum the numbers in each array.




# Example
# Perform summation in the following array over 1st axis:


# Returns: [6 6]