# Python - Escape Characters


# Escape Character


# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.




print("")
txt = "We are the so-called \"Vikings\" from the north."
print(txt)





print("")
print("Single Quote : \\\'")
txt1 = 'It\'s alright.'
print(txt1)





print("")
print("Backslash : \\\\")
txt2 = "This will insert one \\ (backslash)."
print(txt2)






print("")
print("New Line : \\n ")
txt3 = "Hello\nWorld!"
print(txt3)




print("")
print("Carriage Return : \\r ")
txt4 = "Hello\rWorld!"
print(txt4)




print("")
print("Tab : \\t")
txt5 = "Hello\tWorld!"
print(txt5)







#

print("")
print("Backspace : \\b ")
print("This example erases one character (backspace):")
txt6 = "Hello \bWorld!"
print(txt6)






print("")
print("Octal value")
print("")
print("A backslash followed by three integers will result in a octal value : \\...\\...")
print("")
txt7 = "\110\145\154\154\157"
print(txt7)






print("")
print("Hex value")
print("A backslash followed by an 'x' and a hex number represents a hex value : \\x..\\x..")
print("")
txt8 = "\x48\x65\x6c\x6c\x6f"
print(txt8)


print("")


