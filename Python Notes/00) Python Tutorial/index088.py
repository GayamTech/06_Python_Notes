# Since the try block raises an error, the except block will be executed.

# Without the try block, the program will crash and raise an error:

#  Raise an exception

#  As a Python developer you can choose to throw an exception if a condition occurs.

#  To throw (or raise) an exception, use the raise keyword.

#  Example

#  Raise an error and stop the program if x is lower than 0:


print(" ")


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")



# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.

# Example
# Raise a TypeError if x is not an integer:


print(" ")


y = "hello"

if not type(y) is int:
  raise TypeError("Only integers are allowed")


  print(" ")