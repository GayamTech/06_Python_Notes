# Python - Remove Set Items



# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

# Example
# Remove "banana" by using the remove() method:


# Note: If the item to remove does not exist, remove() will raise an error.



thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)













# Example
# Remove "banana" by using the discard() method:

#  Note: If the item to remove does not exist, discard() will NOT raise an error.


thisset1 = {"apple", "banana", "cherry"}

thisset1.discard("banana")

print(thisset1)








# You can also use the pop() method to remove an item, but this method will remove the last item. Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.

# Example
# Remove the last item by using the pop() method:


# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.


thisset2 = {"apple", "banana", "cherry"}

x = thisset2.pop()

print(x) #removed item

print(thisset2) #the set after removal










# Example
# The clear() method empties the set:



thisset3 = {"apple", "banana", "cherry"}

thisset3.clear()

print(thisset3)











# Example
# The del keyword will delete the set completely:




thisset4 = {"apple", "banana", "cherry"}

del thisset4

print(thisset4) #this will raise an error because the set no longer exists













# Python - Loop Sets



# Loop Items
# You can loop through the set items by using a for loop:

# Example
# Loop through the set, and print the values:



thisset5 = {"apple", "banana", "cherry"}

for x in thisset5:
  print(x)
  
  
  
  
  
  
  
  
  
  





