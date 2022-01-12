
# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Make a copy of a dictionary with the copy() method:



thisdict26 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict26.copy()
print(mydict)











# Another way to make a copy is to use the built-in function dict().

# Make a copy of a dictionary with the dict() function:



thisdict27 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict1 = dict(thisdict27)
print(mydict1)
















# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

# Example
# Create a dictionary that contain three dictionaries:


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}













# Or, if you want to add three dictionaries into a new dictionary:

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:



child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily1 = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily1)
