import numpy as np

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)



# Check if Array Owns its Data

# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute base that returns None if the array owns the data.

# Otherwise, the base  attribute refers to the original object.

# Example
# Print the value of the base attribute to check if an array owns it's data or not:



# The copy returns None.
# The view returns the original array