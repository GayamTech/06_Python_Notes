# Access Tuple Items
# You can access tuple items by referring to the index number, inside square brackets:

# Example
# Print the second item in the tuple:




# Note: The first item has index 0.


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])









# Negative Indexing
# Negative indexing means start from the end.

# -1 refers to the last item, -2 refers to the second last item etc.

# Example
# Print the last item of the tuple:


thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[-1])










# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.

# Example
# Return the third, fourth, and fifth item:


# Note: The search will start at index 2 (included) and end at index 5 (not included).



thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included













# By leaving out the start value, the range will start at the first item:

# Example
# This example returns the items from the beginning to, but NOT included, "kiwi":


thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple3[:4])













# By leaving out the end value, the range will go on to the end of the list:

# Example
# This example returns the items from "cherry" and to the end:



thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(thistuple4[2:])











# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the tuple:

# Example
# This example returns the items from index -4 (included) to index -1 (excluded)



thistuple5 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple5[-4:-1])

#Negative indexing means starting from the end of the tuple.

#This example returns the items from index -4 (included) to index -1 (excluded)

#Remember that the last item has the index -1,









# Check if Item Exists
# To determine if a specified item is present in a tuple use the in keyword:

# Example
# Check if "apple" is present in the tuple:



thistuple6 = ("apple", "banana", "cherry")
if "apple" in thistuple6:
  print("Yes, 'apple' is in the fruits tuple")


