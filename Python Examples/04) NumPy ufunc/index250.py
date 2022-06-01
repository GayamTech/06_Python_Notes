import numpy as np

arr = np.array([1, 2, 3])

newarr = np.cumsum(arr)

print(newarr)





# Cummulative Sum


# Cummulative sum means partially adding the elements in array.

# E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

# Perfom partial sum with the cumsum() function.




# Example
# Perform cummulative summation in the following array:




# Returns: [1 3 6]