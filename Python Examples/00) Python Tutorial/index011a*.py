# LIST:                          [
# TUPLE:                         (
# DICTIONARY:                    { Key : Value,
# SET:                           {
# 1) List is a collection which is ordered and changeable. Allows duplicate members.
# 2) Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3) Dictionary is a collection which is unordered, changeable and indexed. No duplicate  members.
# 4) Set is a collection which is unordered and unindexed. No duplicate members.










# List
# Ordered sequence of objects
# In square brackets

print("")
print("List : ")
print("")
print("Ordered, changeable, allows duplicates")
print("")
print("Two ways to decalre a list : []   or   list(())")
h = ["apple", "banana", "cherry"]
y = list(("apple", "banana", "cherry", "apple"))



print("")
print(h)
print(type(h))
print("")
print(y)
print(type(y))



print("")

print("")
print("")

print("Properties of Lists (11) : ")
print("")
print("1) Can be concatenated ")
print("")
print("2) CAN CONTAIN DIFFERENT TYPES   (int, string, float)")
print("")
print("3) To Declare a list : my_list = ['Hello', 1, 3.14] ")

print("")
my_list = ["Hello", 1, 3.14]
print(my_list)
print("")

print("")
print("4) Can be indexed : my_list[0]")
print("0th Index : " + my_list[0])
print("")
print("")

print("5) Can be spliced : my_list[1:]")
print("Splicing from 1st Index to the end : ")
print(my_list[1:])
print("")
print("")

# (starts from the 1st index to the end)


print("6) Can add elements : my_list.append(7) ")
my_list.append(7)
print("Appended list : ")
print(my_list)
print("")
print("")


print("7) Can remove elements :  my_list.pop() ")
my_list.pop()
print("  Popped list (pops from end): ")
print(my_list)
print("")
print("")
# Removes from the end


print(" Remove Elements with the index specified")
my_list.pop(0)
print("  Popped list (specified to pop from top) : my_list.pop(0) ")
print(my_list)
print("")
print("")



print("8) Can be sorted : new_list.sort()")
print(" New List: ")
new_list = [74, 1, 3.14, 42, 56, 13, 11, 14, 5864]
print(new_list)
print("")
new_list.sort()
print(" Sorted List : ")
print(new_list)
print("")
print("")


print("9) Can be reversed : new_list.reverse()")
new_list.reverse()
print(" Reverse Sorted List : ")
print(new_list)
print("")
print("")
print("")
print("10) Can find type : type(my_sorted_list)")
print("")
print("11) Can have nested lists")
print("")
print("Add E, Concatinated, Indexed, Nested, Remove E, Reversed, Sorted, Spliced, Type Checked,")


print("")
print("")
list = [1,1,1,1,1,1,1,2,3,3,3,4,5,5,5,5,5,6]
s = set(list)
print("Example of a List vs. Set : ")
print(" list = [1,1,1,1,1,1,1,2,3,3,3,4,5,5,5,5,5,6] ")
print("set(list)")
print(s)
print("")

