import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])




# Split Into Arrays
# The return value of the array_split() method is an array containing each of the split as an array.

# If you split an array into 3 arrays, you can access them from the result just like any array element:



# Example
# Access the splitted arrays:
