
# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# Update the "year" of the car by using the update() method:



thisdict13 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict13.update({"year": 2020})

print(thisdict13)













# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:


thisdict14 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict14["color"] = "red"
print(thisdict14)













# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

# The argument must be a dictionary, or an iterable object with key:value pairs.

# Add a color item to the dictionary by using the update() method:


thisdict15 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict15.update({"color": "red"})

print(thisdict15)
















# Removing Items
# There are several methods to remove items from a dictionary:

# The pop() method removes the item with the specified key name:

thisdict16 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict16.pop("model")
print(thisdict16)














# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):


thisdict17 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict17.popitem()
print(thisdict17)













# Example
# The del keyword removes the item with the specified key name:

thisdict18 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict18["model"]
print(thisdict18)
















# Example
# The del keyword can also delete the dictionary completely:


thisdict19 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict19
print(thisdict19) #this will cause an error because "thisdict" no longer exists.



















# Example
# The clear() method empties the dictionary:

thisdict20 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict20.clear()
print(thisdict20)












# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Example
# Print all key names in the dictionary, one by one:


thisdict21 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for h in thisdict21:
  print(h)












# Example
# Print all values in the dictionary, one by one:


thisdict22 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for i in thisdict22:
  print(thisdict22[i])
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# Example
# You can also use the values() method to return values of a dictionary:


thisdict23 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for j in thisdict23.values():
  print(j)











# Example
# You can use the keys() method to return the keys of a dictionary:

thisdict24 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for k in thisdict24.keys():
  print(k)















# Example
# Loop through both keys and values, by using the items() method:



thisdict25 =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for l, m in thisdict25.items():
  print(l, m)













