import numpy as np

arr = np.array([20, 8, 32, 36, 16])

x = np.gcd.reduce(arr)

print(x)




# Finding GCD in Arrays
# To find the Highest Common Factor of all values in an array, you can use the reduce() method.

# The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.






# Example
# Find the GCD for all of the numbers in following array:



# Returns: 4 because that is the highest number all values can be divided by.