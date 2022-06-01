# Python Strings

print("")

print("You can use double or single quotes: ")
print("Hello")
print('Hello')





print("")
print("Assign String to a Variable : ")
a = "Hello"
print(a)


print("")


print("")
print("Multiline Strings : ")
print("")
print(" You can use three double quotes Or three single quotes ")
print("")
print("")




a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

print("")

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)



print("")



print("")
print("Strings are Arrays")
print("")
print(" Square brackets can be used to access elements of the string. :  a[1] ")
print("")


a = "Hello, World!"
print(a[1])




print("")



print("")
print("Looping Through a String")
print("")
print(" Loop through the characters in a string, with a for loop.")
print("")
print(" Loop through the letters in the word banana : ")
print("  for x in banana: print(x)")


for x in "banana":
  print(x)




print("")
print("")
print("String Length")
print("")
print(" The len() function returns the length of a string : len(a)")

a = "Hello, World!"
print(len(a))




print("")
print("")
print("Check String")
print("")
print(" To check if a certain phrase or character is present in a string : use the keyword in")
print("")
print(" Check if free is present in the following text : print('free' in txt) ")

txt = "The best things in life are free!"
print("free" in txt)



print("")
print("")
print("Print only if free is present : if 'free' in txt: print('...')")



txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
  

  
print("")
print("")
print("Check if NOT")
print("")
print(" To check if a certain phrase or character is NOT present in string : use keyword not in.")
print("")
print(" Check if expensive is NOT present in the following text : print('expensive' not in txt)")


txt = "The best things in life are free!"
print("expensive" not in txt)




print("")
print("")
print("Use it in an if statement:")
print("")
print("Print only if expensive is NOT present : if 'expensive not in txt: print('...')")



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


print("")
