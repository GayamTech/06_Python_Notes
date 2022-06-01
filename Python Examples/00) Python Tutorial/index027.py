 
# Python Lists




# List items are ordered, changeable, and allow duplicate values.

# ORDERED: If you add new items to a list, the new items will be placed at the end of the list.


# changeable : can change, add, and remove items in a list after it has been created.


# duplicate : can have items with the same value










# Change Item Value

# To change the value of a specific item, refer to the index number:

# Change the second item:




print("")






thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)








print("")









# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:



# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":





thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist1[1:3] = ["blackcurrant", "watermelon"]

print(thislist1)











print("")











# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:


# Change the second value by replacing it with two new values:



thislist2 = ["apple", "banana", "cherry"]

thislist2[1:2] = ["blackcurrant", "watermelon"]

print(thislist2)



# Note: The length of the list will change when the number of items inserted does not match the number of items replaced.














print("")







# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:


# Change the second and third value by replacing it with one value:







thislist3 = ["apple", "banana", "cherry"]

thislist3[1:3] = ["watermelon"]

print(thislist3)








print("")






# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# Insert "watermelon" as the third item:




thislist4 = ["apple", "banana", "cherry"]

thislist4.insert(2, "watermelon")

print(thislist4)




# Note: As a result of the example above, the list will now contain 4 items.


print("")


# To add an item to the end of the list, use the append() method:
# Using the append() method to append an item:




thislist5 = ["apple", "banana", "cherry"]

thislist5.append("orange")

print(thislist5)







print("")





# Insert Items
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:

# Insert an item as the second position:



thislist6 = ["apple", "banana", "cherry"]
thislist6.insert(1, "orange")
print(thislist6)





# Note: As a result of the examples above, the lists will now contain 4 items.









print("")





# Extend List
#To append elements from another list to the current list, use the extend() method.


# Add the elements of tropical to thislist:


# The elements will be added to the end of the list.



thislist7 = ["apple", "banana", "cherry"]
tropical1 = ["mango", "pineapple", "papaya"]

thislist7.extend(tropical1)

print(thislist7)







print("")




# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).


# Add elements of a tuple to a list:




thislist8 = ["apple", "banana", "cherry"]
thistuple1 = ("kiwi", "orange")

thislist.extend(thistuple1)

print(thislist8)





print("")
print("")
print("")
