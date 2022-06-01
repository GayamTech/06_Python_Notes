import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31

print(arr)
print(x)




# Make Changes in the VIEW:


# Example
# Make a view, change the view, and display both arrays:


# The original array SHOULD be affected by the changes made to the view.