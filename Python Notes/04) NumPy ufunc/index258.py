import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)




# Finding LCM in Arrays
# To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.

# The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.





# Example
# Find the LCM of the values of the following array:





# Returns: 18 because that is the lowest common multiple of all three numbers (3*6=18, 6*3=18 and 9*2=18).