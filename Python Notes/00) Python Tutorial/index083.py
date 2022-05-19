# Python RegEx
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.



# RegEx Module
# Python has a built-in package called re, which can be used to work with Regular Expressions.

# Import the re module:

# import re


# RegEx in Python
# When you have imported the re module, you can start using regular expressions:

# Example
# Search the string to see if it starts with "The" and ends with "Spain":




import re

#Check if the string starts with "The" and ends with "Spain":


print(" ")


txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
  

  
print(" ")
  
  
  




# RegEx Functions
# The re module offers a set of functions that allows us to search a string for a match:

#       Function            Description

#       findall             Returns a list containing all matches

#       search              Returns a Match object if there is a match
                                # anywhere in the string
#       split               Returns a list where the string has been split at
                                # each match
#       sub                 Replaces one or many matches with a string




# Metacharacters
# Metacharacters are characters with a special meaning:

#   Character       Description                                 Example

#       []          A set of characters                         "[a-m]"

#       \           Signals a special sequence (can also be used to escape special characters)                                          "\d"

#       .           Any character (except newline character)    "he..o"

#       ^           Starts with                                 "^hello"
#       $           Ends with                                   "planet$"
#       *           Zero or more occurrences                    "he.*o"
#       +           One or more occurrences                     "he.+o"
#       ?           Zero or one occurrences                     "he.?o"
#       {}          Exactly the specified number of occurrences    "he{2}o"
#       |           Either or                               "falls|stays"
#       ()          Capture and group




#   []


print(" ")

txt1 = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x1 = re.findall("[a-m]", txt1)
print(x1)





print(" ")

#   \

txt2 = "That will be 59 dollars"

#Find all digit characters:

x2 = re.findall("\d", txt2)
print(x2)





print(" ")

#   .

txt3 = "hello planet"

#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":

x3 = re.findall("he..o", txt3)
print(x3)








print(" ")
#   ^

txt4 = "hello planet"

#Check if the string starts with 'hello':

x4 = re.findall("^hello", txt4)
if x4:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")







print(" ")

#   $

txt5 = "hello planet"

#Check if the string ends with 'planet':

x5 = re.findall("planet$", txt5)
if x5:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")









print(" ")
#   *


txt6 = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

x6 = re.findall("he.*o", txt6)

print(x6)






print(" ")

#   +


txt7 = "hello planet"

#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

x7 = re.findall("he.+o", txt7)

print(x7)








print(" ")
#   ?



txt8 = "hello planet"

#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x8 = re.findall("he.?o", txt8)

print(x8)

#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"






print(" ")

#   {}




txt9 = "hello planet"

#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

x9 = re.findall("he.{2}o", txt9)

print(x9)








print(" ")
#   |



txt0 = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x0 = re.findall("falls|stays", txt0)

print(x0)

if x0:
  print("Yes, there is at least one match!")
else:
  print("No match")

print(" ")