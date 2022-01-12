# Python Lists




# List items are ordered, changeable, and allow duplicate values.

# ORDERED: If you add new items to a list, the new items will be placed at the end of the list.


# changeable : can change, add, and remove items in a list after it has been created.


# duplicate : can have items with the same value


# Lists are created using square brackets:


print("")




thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)



print("")



# Print the number of items in the list:
print(len(thislist))



print("")

# List items can be of any data type  :   String, int and boolean





list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:


list4 = ["abc", 34, True, 40, "male"]



print(list1)
print(list2)
print(list3)
print(list4)






print("")

# TYPE: lists are defined as objects with the data type 'list':
    #   <class 'list'>





print(type(list1))
print(type(list2))
print(type(list3))
print(type(list4))


print("")
print("")








# Using the list() constructor to make a List:



thislist_X = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist_X)









print("")








# Return the third, fourth, and fifth item:

thislist_y = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist_y)
print(thislist_y[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included








print("")








#This will return the items from index 0 to index 4.

#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included


thislist_z = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist_z)
print(thislist_z[:4])













print("")













#Negative indexing means starting from the end of the list.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,






thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])








print("")












# To determine if a specified item is present in a list use the in keyword:

# Check if "apple" is present in the list:


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")








print("")
