import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)
      
      
      
      
      
      
      
# To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# Example
# Iterate down to the scalars:


