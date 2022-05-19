import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)

print(newarr)




# NumPy Differences


# Differences

# A discrete difference means subtracting two successive elements.

# E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]

# To find the discrete difference, use the diff() function.



# Example
# Compute discrete difference of the following array:



# Returns: [5 10 -20] because 15-10=5, 25-15=10, and 5-25=-20