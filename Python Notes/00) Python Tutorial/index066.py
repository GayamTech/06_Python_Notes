# Import From Module
# You can choose to import only parts from a module, by using the from keyword.




# Example
# The module named mymodule has one function and one dictionary:



# Example
# Import only the person1 dictionary from the module:


# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]






from mymodule2 import person1

print(person1["age"])
