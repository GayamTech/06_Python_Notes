# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Example
# Packing a tuple:


fruits = ("apple", "banana", "cherry")

print(fruits)













# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

# Example
# Unpacking a tuple:

# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.





fruits1 = ("apple", "banana", "cherry")

(green, yellow, red) = fruits1

print(green)
print(yellow)
print(red)












# Using Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

# Example
# Assign the rest of the values as a list called "red":


fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green1, yellow1, *red1) = fruits2

print(green1)
print(yellow1)
print(red1)










# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

# Example
# Add a list of values the "tropic" variable:


fruits3 = ("apple", "mango", "papaya", "pineapple", "cherry")

(green2, *tropic2, red2) = fruits3

print(green2)
print(tropic2)
print(red2)
