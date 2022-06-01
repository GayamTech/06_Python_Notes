#   Sets

# A set is a set of characters inside a pair of square brackets [] with a special meaning:

#       Set                 Description
#       [arn]       Returns a match where one of the
                    #specified characters (a, r, or n) are present

#       [a-n]       Returns a match for any lower case character,
                    #alphabetically between a and n

#       [^arn]      Returns a match for any character EXCEPT a, r, and n

#       [0123]      Returns a match where any of the specified
                    #digits (0, 1, 2, or 3) are present

#       [0-9]       Returns a match for any digit between 0 and 9

#       [0-5][0-9]    Returns a match for any two-digit numbers from 00 and 59

#       [a-zA-Z]    Returns a match for any character alphabetically
                    #between a and z, lower case OR upper case

#       [+]         In sets, +, *, ., |, (), $,{} has no special
                    #meaning, so [+] means: return a match for
                    #any + character in the string










# [arn]


import re


print(" ")


txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")





print(" ")

# [a-n]


txt1 = "The rain in Spain"

#Check if the string has any characters between a and n:

x1 = re.findall("[a-n]", txt1)

print(x1)

if x1:
  print("Yes, there is at least one match!")
else:
  print("No match")







print(" ")

# [^arn]


txt2 = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x2 = re.findall("[^arn]", txt2)

print(x2)

if x2:
  print("Yes, there is at least one match!")
else:
  print("No match")









print(" ")

# [0123]


txt3 = "The rain in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x3 = re.findall("[0123]", txt3)

print(x3)

if x3:
  print("Yes, there is at least one match!")
else:
  print("No match")











print(" ")

# [0-9]



txt4 = "8 times before 11:45 AM"

#Check if the string has any digits:

x4 = re.findall("[0-9]", txt4)

print(x4)

if x4:
  print("Yes, there is at least one match!")
else:
  print("No match")









print(" ")

# [0-5][0-9]


txt5 = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x5 = re.findall("[0-5][0-9]", txt5)

print(x5)

if x5:
  print("Yes, there is at least one match!")
else:
  print("No match")






print(" ")

# [a-zA-Z]



txt6 = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x6 = re.findall("[a-zA-Z]", txt6)

print(x6)

if x6:
  print("Yes, there is at least one match!")
else:
  print("No match")








print(" ")


# [+]



txt7 = "8 times before 11:45 AM"

#Check if the string has any + characters:

x7 = re.findall("[+]", txt7)

print(x7)

if x7:
  print("Yes, there is at least one match!")
else:
  print("No match")


print(" ")