import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

newarr = np.subtract(arr1, arr2)

print(newarr)




# Subtraction

# The subtract() function subtracts the values from one array with the values from another array, and return the results in a new array.






# Example
# Subtract the values in arr2 from the values in arr1:



# The example above will return [-10 -1 8 17 26 35] which is the result of 10-20, 20-21, 30-22 etc.