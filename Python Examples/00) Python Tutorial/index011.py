# Python Data Types


# Text Type:         str
# Numeric Types:     int, float, complex
# Sequence Types:    list, tuple, range
# Mapping Type:      dict
# Set Types:         set, frozenset
# Boolean Type:      bool
# Binary Types:      bytes, bytearray, memoryview


print("")
x = 5
print(type(x))



# list
h = ["apple", "banana", "cherry"]
y = list(("apple", "banana", "cherry", "apple"))

#display y:
print(y)

#display the data type of y:
print(type(y))

print(h)
print(type(h))



# Tuples are immutable, used when your using objects that need to be passed around & you want to make sure they wont be changed (DATA INTEGRITY)

# Lists can be changed

# Tuples use ( ; Lists use [







# tuple
# Ordered IMMUTABLE objects in a list
# In parenthesis

g = ("apple", "banana", "cherry")
z = tuple(("apple", "banana", "cherry", "apple"))

#display z:
print(z)

#display the data type of z:
print(type(z))

print(g)
print(type(g))





# range


a = range(6)

#display a:
print(a)

#display the data type of a:
print(type(a))








# dict

b = dict(name="John", age=36)

#display b:
print(b)

#display the data type of b:
print(type(b))







# set : Duplicates are DELETED
# Unique unordered objects
# In curly brackets

e = {"apple", "banana", "cherry"}
c = set(("apple", "banana", "cherry", "apple"))

#display c:
print(c)

#display the data type of c:
print(type(c))

print(e)
print(type(e))







# frozenset


d = frozenset(("apple", "banana", "cherry", "apple"))

#display d:
print(d)

#display the data type of d:
print(type(d))





list = [1,1,1,1,1,1,1,2,3,3,3,4,5,5,5,5,5,6]
s = set(list)
print(s)




# LIST:                          [
# TUPLE:                         (
# SET:                           {
# DICTIONARY:                    { Key : Value,
# 1) List is a collection which is ordered and changeable. Allows duplicate members.
# 2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3) Set is a collection which is unordered and unindexed. No duplicate members.
# 4) Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
