import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 6, 8, 2, 33])

newarr = np.power(arr1, arr2)

print(newarr)




# Power
# The power() function rises the values from the first array to the power of the values of the second array, and return the results in a new array.




# Example
# Raise the valules in arr1 to the power of values in arr2:




# The example above will return [1000 3200000 729000000 6553600000000 2500 0] which is the result of 10*10*10, 20*20*20*20*20, 30*30*30*30*30*30 etc.