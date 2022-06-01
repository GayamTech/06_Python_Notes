# LIST:                          [
# TUPLE:                         (
# DICTIONARY:                    { Key : Value,
# SET:                           {
# 1) List is a collection which is ordered and changeable. Allows duplicate members.
# 2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3) Dictionary is a collection which is unordered, changeable and indexed. No duplicate  members.
# 4) Set is a collection which is unordered and unindexed. No duplicate members.




# tuple
# Ordered IMMUTABLE objects in a list
# In parenthesis

print("")
print("Tuple : ")
print("")
print("Ordered, IMMUTABLE, allows duplicates")
print("")
print("Two ways to decalre a Tuple :    ()   or   tuple(())")

g = ("apple", "banana", "cherry")
z = tuple(("apple", "banana", "cherry", "apple"))



print("")
print(g)
print(type(g))
print("")
print(z)
print(type(z))
print("")
print("")
print("")
print("Properties of Tupules (5)")
print("")
print("1)   Can contain multiple types (String, Int, Float, List)")
print("")
print("2)   Can be indexed & reverse indexed")
print("")
print("3)   Can be sliced")
print("")
print("4)   Can count the amount of times an object is in the tuple")
print("")
print(" z.count('apple'): returns the number of times apple shows up in the tuple")
print("")
print(z.count('apple'))
print("")
print("5)   Can find first location of object : z.index('apple')")
print("")
print(z.index('apple'))
print("")
print("")
