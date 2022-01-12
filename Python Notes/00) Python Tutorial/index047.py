# Python Dictionaries

# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:

# Create and print a dictionary:


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)










# Dictionary Items

# Dictionary items are ordered, changeable, and does not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Print the "brand" value of the dictionary:

thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict1["brand"])












# Ordered or Unordered?

# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values:



thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict2)















# Dictionary Length
# To determine how many items a dictionary has, use the len() function:

# Print the number of items in the dictionary:

thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict3))











# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:

# String, int, boolean, and list data types:


thisdict4 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict4)













# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':

# <class 'dict'>

# Print the data type of a dictionary:



thisdict5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict5))












# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:

# Get the value of the "model" key:

thisdict6 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict6["model"]
print(x)












# There is also a method called get() that will give you the same result:

# Get the value of the "model" key:



thisdict7 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
y = thisdict7.get("model")
print(y)















# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

# Get a list of the keys:


thisdict8 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

z = thisdict8.keys()

print(z)














# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Add a new item to the original dictionary, and see that the keys list gets updated as well:


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

a = car.keys()

print(a) #before the change

car["color"] = "white"

print(a) #after the change
















# Get Values
# The values() method will return a list of all the values in the dictionary.

# Get a list of the values:

thisdict9 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

b = thisdict9.values()

print(b)













# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

# Make a change in the original dictionary, and see that the values list gets updated as well:


car1 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

c = car1.values()

print(c) #before the change

car["year"] = 2020

print(c) #after the change












# Example
# Add a new item to the original dictionary, and see that the values list gets updated as well:

car2 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

d = car2.values()

print(d) #before the change

car["color"] = "red"

print(d) #after the change













# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.


# Get a list of the key:value pairs



thisdict10 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

e = thisdict10.items()

print(e)








# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.

# Make a change in the original dictionary, and see that the items list gets updated as well:


car3 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

f = car3.items()

print(f) #before the change

car["year"] = 2020

print(f) #after the change











# Example
# Add a new item to the original dictionary, and see that the items list gets updated as well:


car4 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

g = car4.items()

print(g) #before the change

car["color"] = "red"

print(g) #after the change













# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:

# Check if "model" is present in the dictionary:



thisdict11 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict11:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")














# Change Values
# You can change the value of a specific item by referring to its key name:

# Change the "year" to 2018:


thisdict12 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict12["year"] = 2018

print(thisdict12)













