import numpy as np

arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 7, 9, 8, 2, 33])

newarr = np.divmod(arr1, arr2)

print(newarr)




# Quotient and Mod

# The divmod() function return both the quotient and the the mod. The return value is two arrays, the first array contains the quotient and second array contains the mod.

# Example
# Return the quotient and mod:





# The example above will return:
# (array([3, 2, 3, 5, 25, 1]), array([1, 6, 3, 0, 0, 27]))
# The first array represents the quotients, (the integer value when you divide 10 with 3, 20 with 7, 30 with 9 etc.
# The second array represents the remainders of the same divisions.
