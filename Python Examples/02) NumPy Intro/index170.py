import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)




# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

# The searchsorted() method is assumed to be used on sorted arrays.

# Example
# Find the indexes where the value 7 should be inserted:




# Example explained: The number 7 should be inserted on index 1 to remain the sort order.

# The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.