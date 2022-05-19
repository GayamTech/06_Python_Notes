import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print(newarr)




# The example above returns three 2-D arrays.

# In addition, you can specify which axis you want to do the split around.

# The example below also returns three 2-D arrays, but they are split along the row (axis=1).

# Example
# Split the 2-D array into three 2-D arrays along rows.
