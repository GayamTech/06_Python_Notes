# Python - Slicing Strings





print("")
print("Slicing")
print("")
print("You can return a range of characters by using the slice syntax.")
print("")
print("Specify the start index and the end index, separated by a colon, to return a part of the string.")
print("")
print("")
print("Get the characters from position 2 to position 5 (not included): b[2:5]")
print("")
print("Note: The first character has index 0.")
print("")
print("")
b = "Hello, World!"
print(b[2:5])

print("")
print("")
print("Slice From the Start")
print("")
print("By leaving out the start index, the range will start at the first character : ")
print("")
print("Get the characters from the start to position 5 (not included) : b[:5]")
print("")





b = "Hello, World!"
print(b[:5])


print("")
print("")
print("Slice To the End")
print("")
print("By leaving out the end index, the range will go to the end:")
print("")
print("Get the characters from position 2, and all the way to the end: b[2:]")

b = "Hello, World!"
print(b[2:])




print("")
print("")
print("Negative Indexing")
print("")
print("Use negative indexes to start the slice from the end of the string:")
print("")
print("Get the characters:")
print("")
print("From: 'o' in 'World!' (position -5)")
print("")
print("To, but not included: 'd' in 'World!' (position -2) : b[-5:-2]")
print("")


b = "Hello, World!"
print(b[-5:-2])
print("")

