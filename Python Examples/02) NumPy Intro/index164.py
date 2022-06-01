import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)





# The example above returns three 2-D arrays.

# Let's look at another example, this time each element in the 2-D arrays contains 3 elements.

# Example
# Split the 2-D array into three 2-D arrays.
