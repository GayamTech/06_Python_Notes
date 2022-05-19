import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  for y in x:
    print(y)
    
    
# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# Example
# Iterate on each scalar element of the 2-D array:
