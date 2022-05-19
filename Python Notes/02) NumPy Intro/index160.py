import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)




# NumPy Splitting Array


# Splitting NumPy Arrays
# Splitting is reverse operation of Joining.

# Joining merges multiple arrays into one and Splitting breaks one array into multiple.

# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

# Example
# Split the array in 3 parts:


# Note: The return value is an array containing three arrays.