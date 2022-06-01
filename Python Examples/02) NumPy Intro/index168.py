import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)





# The example above will return a tuple: (array([3, 5, 6],)

# Which means that the value 4 is present at index 3, 5, and 6.

# Example
# Find the indexes where the values are even:


