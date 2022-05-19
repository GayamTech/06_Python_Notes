import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)




# Unknown Dimension

# You are allowed to have one "unknown" dimension.

# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.

# Pass -1 as the value, and NumPy will calculate this number for you.

# Example
# Convert 1D array with 8 elements to 3D array with 2x2 elements:




# Note: We can not pass -1 to more than one dimension.
