# Python - Update Tuples


# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there are some workarounds.




# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# Example
# Convert the tuple into a list to be able to change it:



x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)










# Add Items
# Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

# Example
# Convert the tuple into a list, add "orange", and convert it back into a tuple:



thistuple1 = ("apple", "banana", "cherry")
z = list(thistuple1)
z.append("orange")
thistuple1 = tuple(z)

print(thistuple1)












# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

# Example
# Create a new tuple with the value "orange", and add that tuple:

# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.



thistuple2 = ("apple", "banana", "cherry")
a = ("orange",)
thistuple2 += a

print(thistuple2)














# Remove Items
# Note: You cannot remove items in a tuple.

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

# Example
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:



thistuple3 = ("apple", "banana", "cherry")
b = list(thistuple3)
b.remove("apple")
thistuple3 = tuple(b)

print(thistuple3)













# Or you can delete the tuple completely:

# Example
# The del keyword can delete the tuple completely:



thistuple4 = ("apple", "banana", "cherry")
del thistuple4
#  print(thistuple4) #this will raise an error because the tuple no longer exists







