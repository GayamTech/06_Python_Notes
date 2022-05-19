import numpy as np

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)




# Cummulative Product


# Cummulative product means taking the product partially.

# E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

# Perfom partial sum with the cumprod() function.




# Example
# Take cummulative product of all elements for following array:




# Returns: [5 30 210 1680]