# Python Sets


# Set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

# Sets are written with curly brackets.

# Example
# Create a Set:


# Note: Sets are unordered, so you cannot be sure in which order the items will appear.



thisset = {"apple", "banana", "cherry"}
print(thisset)

# Note: the set list is unordered, meaning: the items will appear in a random order.

# Refresh this page to see the change in the result.







# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Once a set is created, you cannot change its items, but you can remove items and add new items.









# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Example
# Duplicate values will be ignored:



thisset1 = {"apple", "banana", "cherry", "apple"}

print(thisset1)















# Get the Length of a Set
# To determine how many items a set has, use the len() method.

# Example
# Get the number of items in a set:


thisset2 = {"apple", "banana", "cherry"}

print(len(thisset2))












# Set Items - Data Types
# Set items can be of any data type:

# Example
# String, int and boolean data types:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)












# A set can contain different data types:

# Example
# A set with strings, integers and boolean values:




set4 = {"abc", 34, True, 40, "male"}

print(set4)












# type()
# From Python's perspective, sets are defined as objects with the data type 'set':

# <class 'set'>

# Example
# What is the data type of a set?

myset = {"apple", "banana", "cherry"}

print(type(myset))








# The set() Constructor
# It is also possible to use the set() constructor to make a set.

# Example
# Using the set() constructor to make a set:


thisset3 = set(("apple", "banana", "cherry"))
print(thisset3)

# Note: the set list is unordered, so the result will display the items in a random order.










# Python Collections (Arrays)

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
