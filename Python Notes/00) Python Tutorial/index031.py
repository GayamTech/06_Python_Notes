# Python - Sort Lists

# Sort List Alphanumerically

# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:






# Example
# Sort the list alphabetically:



thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)








# Sort the list numerically:

thislist1 = [100, 50, 65, 82, 23]

thislist1.sort()

print(thislist1)








# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# Example
# Sort the list descending:


thislist2 = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist2.sort(reverse = True)

print(thislist2)







# Sort the list descending:


thislist3 = [100, 50, 65, 82, 23]

thislist3.sort(reverse = True)

print(thislist3)











# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):

# Example
# Sort the list based on how close the number is to 50:


def myfunc(n):
  return abs(n - 50)

thislist4 = [100, 50, 65, 82, 23]

thislist4.sort(key = myfunc)

print(thislist4)












# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Example
# Case sensitive sorting can give an unexpected result:


thislist5 = ["banana", "Orange", "Kiwi", "cherry"]

thislist5.sort()

print(thislist5)












# Luckily we can use built-in functions as key functions when sorting a list.

# So if you want a case-insensitive sort function, use str.lower as a key function:

# Example
# Perform a case-insensitive sort of the list:


thislist6 = ["banana", "Orange", "Kiwi", "cherry"]

thislist6.sort(key = str.lower)

print(thislist6)












# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.

# Example
# Reverse the order of the list items:


thislist7 = ["banana", "Orange", "Kiwi", "cherry"]

thislist7.reverse()

print(thislist7)

