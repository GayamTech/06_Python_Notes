# Python - Remove List Items

print("")
print("")



# The remove() method removes the specified item.

# Remove "banana":


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)





print("")







# The pop() method removes the specified index.

# Remove the second item:

thislist1 = ["apple", "banana", "cherry"]
thislist1.pop(1)
print(thislist1)






print("")






# If you do not specify the index, the pop() method removes the last item.

# Remove the last item:


thislist2 = ["apple", "banana", "cherry"]
thislist2.pop()
print(thislist2)







print("")









# The del keyword also removes the specified index:

# Remove the first item:



thislist3 = ["apple", "banana", "cherry"]
del thislist3[0]
print(thislist3)









print("")










# The del keyword can also delete the list completely.

# Delete the entire list:





thislist4 = ["apple", "banana", "cherry"]
del thislist4
print(thislist4) #this will cause an error because you have succsesfully deleted "thislist".






print("")












# Clear the List
# The clear() method empties the list.

# The list still remains, but it has no content.

# Clear the list content:



thislist5 = ["apple", "banana", "cherry"]
thislist5.clear()
print(thislist5)




print("")



