# Python RegEx
# The findall() Function
# The findall() function returns a list containing all matches.

# Example
# Print a list of all matches:


# The list contains the matches in the order they are found.

import re

# Return a list containing every occurrence of "ai":



print(" ")


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)






# If no matches are found, an empty list is returned:

# Example
# Return an empty list if no match was found:

print(" ")


txt1 = "The rain in Spain"

#Check if "Portugal" is in the string:

x1 = re.findall("Portugal", txt1)
print(x1)

if (x1):
  print("Yes, there is at least one match!")
else:
  print("No match")







# The search() Function
# The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:

# Example
# Search for the first white-space character in the string:

print(" ")



txt2 = "The rain in Spain"
x2 = re.search("\s", txt2)

print("The first white-space character is located in position:", x2.start())









# If no matches are found, the value None is returned:

# Example
# Make a search that returns no match:


print(" ")


txt3 = "The rain in Spain"
x3 = re.search("Portugal", txt3)
print(x3)









# The split() Function
# The split() function returns a list where the string has been split at each match:

# Example

#Split the string at every white-space character:


print(" ")

txt4 = "The rain in Spain"
x4 = re.split("\s", txt4)
print(x4)









# You can control the number of occurrences by specifying the maxsplit parameter:

# Example
# Split the string only at the first occurrence:

#Split the string at the first white-space character:


print(" ")


txt5 = "The rain in Spain"
x5 = re.split("\s", txt5, 1)
print(x5)










# The sub() Function
# The sub() function replaces the matches with the text of your choice:

# Example

#Replace all white-space characters with the digit "9":


print(" ")


txt6 = "The rain in Spain"
x6 = re.sub("\s", "9", txt6)
print(x6)










# You can control the number of replacements by specifying the count parameter:

# Example

#Replace the first two occurrences of a white-space character with the digit 9:


print(" ")


txt7 = "The rain in Spain"
x7 = re.sub("\s", "9", txt7, 2)
print(x7)









# Match Object
# A Match Object is an object containing information about the search and the result.

# Note: If there is no match, the value None will be returned, instead of the Match Object.

# Example

#The search() function returns a Match object:


print(" ")


txt8 = "The rain in Spain"
x8 = re.search("ai", txt8)
print(x8)












# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match





# Example
# Print the position (start- and end-position) of the first match occurrence.

# The regular expression looks for any words that starts with an upper case "S":

#Search for an upper case "S" character in the beginning of a word, and print its position:


print(" ")


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())












# Example
# Print the string passed into the function:


#The string property returns the search string:


print(" ")


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)












# Example
# Print the part of the string where there was a match.

# The regular expression looks for any words that starts with an upper case "S":


# Note: If there is no match, the value None will be returned, instead of the Match Object.



#Search for an upper case "S" character in the beginning of a word, and print the word:


print(" ")


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())







print(" ")