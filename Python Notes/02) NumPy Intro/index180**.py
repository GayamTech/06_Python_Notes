import numpy as np

arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)




# Creating Filter Directly From Array
# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.

# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.



# Example
# Create a filter array that will return only values higher than 42:
