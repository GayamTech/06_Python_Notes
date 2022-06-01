# Python - Format - Strings





print("")
print("We can combine strings and numbers by using the format() method!")
print("")
print("The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:")
print("")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


# Arguments

print("")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



print("")
# Placeholders

quantity1 = 3
itemno1 = 567
price1 = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity1, itemno1, price1))
print("")
