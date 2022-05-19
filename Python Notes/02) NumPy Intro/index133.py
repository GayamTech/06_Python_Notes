import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)




# VIEW:


# Example
# Make a view, change the original array, and display both arrays:




# The view SHOULD be affected by the changes made to the original array.
