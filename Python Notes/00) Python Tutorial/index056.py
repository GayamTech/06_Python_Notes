


# Python Arrays


# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.





# Arrays
# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

# Arrays are used to store multiple values in one single variable:

# Create an array containing car names:



print(" ")

cars = ["Ford", "Volvo", "BMW"]

print(cars)













# Access the Elements of an Array
# You refer to an array element by referring to the index number.

# Get the value of the first array item:

print(" ")

cars1 = ["Ford", "Volvo", "BMW"]

x = cars1[0]

print(x)













# Modify the value of the first array item:

print(" ")

cars2 = ["Ford", "Volvo", "BMW"]

cars2[0] = "Toyota"

print(cars2)
















# The Length of an Array
# Use the len() method to return the length of an array (the number of elements in an array).

# Return the number of elements in the cars array:

# Note: The length of an array is always one more than the highest array index.

print(" ")

cars3 = ["Ford", "Volvo", "BMW"]

y = len(cars3)

print(y)

















# Looping Array Elements
# You can use the for in loop to loop through all the elements of an array.

# Print each item in the cars array:

print(" ")


cars4 = ["Ford", "Volvo", "BMW"]

for z in cars4:
  print(z)
















# Adding Array Elements
# You can use the append() method to add an element to an array.

# Add one more element to the cars array:

print(" ")

cars5 = ["Ford", "Volvo", "BMW"]

cars5.append("Honda")

print(cars5)

















# Removing Array Elements
# You can use the pop() method to remove an element from the array.

# Delete the second element of the cars array:

print(" ")

cars6 = ["Ford", "Volvo", "BMW"]

cars6.pop(1)

print(cars6)

















# You can also use the remove() method to remove an element from the array.

# Delete the element that has the value "Volvo":

# Note: The list's remove() method only removes the first occurrence of the specified value.


print(" ")

cars7 = ["Ford", "Volvo", "BMW"]

cars7.remove("Volvo")

print(cars7)



print(" ")






# Array Methods


#  Method    Description

#  append()    Adds an element at the end of the list

#  clear()    Removes all the elements from the list

#  copy()    Returns a copy of the list

#  count()    Returns the number of elements with the specified value

#  extend()    Add the elements of a list (or any iterable), to the end of the current list

# index()    Returns the index of the first element with the specified value

# insert()    Adds an element at the specified position

# pop()    Removes the element at the specified position

# remove()    Removes the first item with the specified value

# reverse()    Reverses the order of the list

# sort()    Sorts the list

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
