import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)




# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.

# We can use reshape(-1) to do this.

# Example
# Convert the array into a 1D array:


# Note: There are a lot of functions for changing the shapes of arrays in numpy flatten, ravel and also for rearranging the elements rot90, flip, fliplr, flipud etc. These fall under Intermediate to Advanced section of numpy.