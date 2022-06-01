import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)




# Splitting 2-D Arrays
# Use the same syntax when splitting 2-D arrays.

# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

# Example
# Split the 2-D array into three 2-D arrays.
