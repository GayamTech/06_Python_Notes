import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)




# Returns Copy or View?

# Example
# Check if the returned array is a copy or a view:


# The example above returns the original array, so it is a view.