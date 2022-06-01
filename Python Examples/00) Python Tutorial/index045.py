# Python - Join Sets


# Join Two Sets
# There are several ways to join two or more sets in Python.

# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:

# Example
# The union() method returns a new set with all items from both sets:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)











# Example
# The update() method inserts the items in set2 into set1:

# Note: Both union() and update() will exclude any duplicate items.


set4 = {"a", "b" , "c"}
set5 = {1, 2, 3}

set4.update(set5)
print(set4)










# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

# Example
# Keep the items that exist in both set x, and set y:



x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)











# The intersection() method will return a new set, that only contains the items that are present in both sets.

# Example
# Return a set that contains the items that exist in both set x, and set y:

a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}

c = a.intersection(b)

print(c)














# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# Example
# Keep the items that are not present in both sets:



d = {"apple", "banana", "cherry"}
e = {"google", "microsoft", "apple"}

d.symmetric_difference_update(e)

print(d)












# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

# Example
# Return a set that contains all items from both sets, except items that are present in both:



e = {"apple", "banana", "cherry"}
f = {"google", "microsoft", "apple"}

g = e.symmetric_difference(f)

print(g)

