import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)



# Iterating With Different Step Size
# We can use filtering and followed by iteration.

# Example
# Iterate through every scalar element of the 2D array skipping 1 element:
