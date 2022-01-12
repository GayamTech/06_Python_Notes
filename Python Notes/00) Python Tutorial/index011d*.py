# LIST:                          [
# TUPLE:                         (
# DICTIONARY:                    { Key : Value,
# SET:                           {
# 1) List is a collection which is ordered and changeable. Allows duplicate members.
# 2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3) Dictionary is a collection which is unordered, changeable and indexed. No duplicate  members.
# 4) Set is a collection which is unordered and unindexed. No duplicate members.




# set : Duplicates are DELETED
# Unique unordered objects
# In curly brackets
print("")
print("Set : ")
print("")
print("Unodered, UNINDEXED, NO Duplicates")
print("")
print("To decalre a Set :    {}   or   set(())")

e = {"apple", "banana", "cherry"}
c = set(("apple", "banana", "cherry", "apple"))

print(e)
print(type(e))
print("")
print(c)
print(type(c))
print("")


print("")
list = [1,1,1,1,1,1,1,2,3,3,3,4,5,5,5,5,5,6]
s = set(list)
print("Example of a List vs. Set : ")
print(" list = [1,1,1,1,1,1,1,2,3,3,3,4,5,5,5,5,5,6] ")
print("set(list)")
print(s)
print("")



print("Adding an element to a set : s.add(7)")
s.add(7)
print(s)
