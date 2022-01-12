# LIST:                          [
# TUPLE:                         (
# DICTIONARY:                    { Key : Value,
# SET:                           {
# 1) List is a collection which is ordered and changeable. Allows duplicate members.
# 2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3) Dictionary is a collection which is unordered, changeable and indexed. No duplicate  members.
# 4) Set is a collection which is unordered and unindexed. No duplicate members.



# Dictionary
# Dictionaries are mappings and do not retain order!
# Unordered key-value pairs
# In curly braces

print("")
print("Dictionary : ")
print("")
print("Unodered, changeable, INDEXED, NO Duplicates")
print("")
print("To decalre a Dictionary :    { Key : Value,}")
b = dict(name="John", age=36)

print("")
print(b)
print(type(b))
print("")
print("")



print("")
print("Properties of Dictionaries (4)")
print("")
print("1)     To grab an object use keys NOT INDEXING")
print("")
print("2)     CANNOT BE SORTED")
print("")
print("3)     Values can be of different types (int, string, float, LISTS, dictionaries)")
print("")
print("4)     Can contain dictionaries (Nested Dictionaries)")
print("")


d = {'k1':123, 'k2':[0,1,2], 'k3':('insideKey')}

print("")
print("Nested Dictionaries Example : ")
print("")
print("What does each return")
print("")
print("d = { 'k1':123, 'k2':[0,1,2], 'k3':('insideKey')}")
print("")
print("a) d['k2'][2]")
print(d['k2'][2])
print("")
print("b) d['k3']")
print(d['k3'])
print("")
print("")

print("Adding an element to a dictionary : d['k4']=300")
d['k4']=300
print(d)
print("")

# Dictionary vs List

# List can be indexed, so can be spliced / sorted
# Dictionaries use keys so don't need to know location to pull out value (FASTER/EASIER)
# But dictionaries cannot be spliced / sorted
