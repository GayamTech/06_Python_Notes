# Python String Formatting

# To make sure a string will display as expected, we can format the result with the format() method.

# String format()
# The format() method allows you to format selected parts of a string.

# Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

# To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

# Example
# Add a placeholder where you want to display the price:


price = 49
txt = "The price is {} dollars"
print(txt.format(price))









# You can add parameters inside the curly brackets to specify how to convert the value:

# Example
# Format the price to be displayed as a number with two decimals:


price1 = 49
txt1 = "The price is {:.2f} dollars"
print(txt1.format(price1))










# Multiple Values
# If you want to use more values, just add more values to the format() method:

# print(txt.format(price, itemno, count))
# And add more placeholders:

# Example




quantity = 3
itemno = 567
price2 = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price2))















# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

# Example


quantity1 = 3
itemno1 = 567
price3 = 49
myorder1 = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder1.format(quantity1, itemno1, price3))











# Also, if you want to refer to the same value more than once, use the index number:

# Example

age = 36
name = "John"
txt2 = "His name is {1}. {1} is {0} years old."
print(txt2.format(age, name))









# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

# Example


myorder2 = "I have a {carname}, it is a {model}."
print(myorder2.format(carname = "Ford", model = "Mustang"))

