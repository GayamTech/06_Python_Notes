import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')

print(x)







# Search From the Right Side


# By default the left most index is returned, but we can give side='right' to return the right most index instead.

# Example
# Find the indexes where the value 7 should be inserted, starting from the right:



# Example explained: The number 7 should be inserted on index 2 to remain the sort order.

# The method starts the search from the right and returns the first index where the number 7 is no longer less than the next value.
