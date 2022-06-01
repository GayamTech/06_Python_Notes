# Python - List Comprehension


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:









fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)







#With list comprehension you can do all that with only one line of code:



fruits1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist1 = [x for x in fruits1 if "a" in x]

print(newlist1)






# The Syntax
# newlist = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.





# Condition
# The condition is like a filter that only accepts the items that valuate to True.

# Example
# Only accept items that are not "apple":


fruits2 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist2 = [x for x in fruits2 if x != "apple"]

print(newlist2)










# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:

# With no if statement:




fruits3 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist3 = [x for x in fruits3]

print(newlist3)










# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc.

# Example
# You can use the range() function to create an iterable:




newlist4 = [x for x in range(10)]

print(newlist4)
















# Same example, but with a condition:

# Example
# Accept only numbers lower than 5:



newlist5 = [x for x in range(10) if x < 5]

print(newlist5)










# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

# Example
# Set the values in the new list to upper case:



fruits6 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist6 = [x.upper() for x in fruits6]

print(newlist6)













# You can set the outcome to whatever you like:

# Example
# Set all values in the new list to 'hello':


fruits7 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist7 = ['hello' for x in fruits7]

print(newlist7)















# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# Example
# Return "orange" instead of "banana":

# The expression in the example above says:

# "Return the item if it is not banana, if it is banana return orange".



fruits8 = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist8 = [x if x != "banana" else "orange" for x in fruits8]

print(newlist8)
