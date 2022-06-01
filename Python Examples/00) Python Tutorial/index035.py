# Python Tuples



# Tuple

# Tuples are used to store multiple items in a single variable.


# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Create a Tuple:




thistuple = ("apple", "banana", "cherry")
print(thistuple)









# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.

# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

# Unchangeable
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Example
# Tuples allow duplicate values:




thistuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple1)













# Tuple Length
# To determine how many items a tuple has, use the len() function:

# Example
# Print the number of items in the tuple:


thistuple2 = tuple(("apple", "banana", "cherry"))
print(len(thistuple2))











# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

# Example
# One item tuple, remember the comma:




thistuple3 = ("apple",)
print(type(thistuple3))

#NOT a tuple
thistuple4 = ("apple")
print(type(thistuple4))









# Tuple Items - Data Types
# Tuple items can be of any data type:

# Example
# String, int and boolean data types:

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)













# A tuple can contain different data types:

# Example
# A tuple with strings, integers and boolean values:

tuple4 = ("abc", 34, True, 40, "male")

print(tuple4)














# type()
# From Python's perspective, tuples are defined as objects with the data type 'tuple':

# <class 'tuple'>

# Example
# What is the data type of a tuple?


mytuple5 = ("apple", "banana", "cherry")

print(type(mytuple5))















# The tuple() Constructor
# It is also possible to use the tuple() constructor to make a tuple.

# Example
# Using the tuple() method to make a tuple:



thistuple5 = tuple(("apple", "banana", "cherry"))
                # note the double round-brackets
print(thistuple5)

















# List is a collection which is ordered and changeable. Allows duplicate members.

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# Dictionary is a collection which is ordered** and changeable. No duplicate members.
