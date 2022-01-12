#Python RegEx


#   Special Sequences
# A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

#       Character       Description
#       \A              Returns a match if the specified characters are at                        the beginning of the string

#       \b              Returns a match where the specified characters are at                     the beginning or at the end of a word (the "r" in the                     beginning is making sure that the string is being                         treated as a "raw string")
                                                        
                                                        
#       \B              Returns a match where the specified characters are                        present, but NOT at the beginning (or at the end) of                      a word (the "r" in the beginning is making sure that                      the string is being treated as a "raw string")
                                                        

#       \d              Returns a match where the string contains digits
                        #(numbers from 0-9)

#       \D              Returns a match where the
                        #string DOES NOT contain digits

#       \s              Returns a match where the string
                        #contains a white space character

#       \S              Returns a match where the string
                        #DOES NOT contain a white space
                        #character

#       \w              Returns a match where the string
                        #contains any word characters
                        #(characters from a to Z, digits
                        #from 0-9, and the underscore _
                        #character)

#       \W              Returns a match where the string
                        #DOES NOT contain any word
                        #characters

#       \Z              Returns a match if the specified
                        #characters are at the end of
                        #the string





#   \A

import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
  
  
  
  
  
  
  
  
  
#   \b


txt1 = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x1 = re.findall(r"\bain", txt1)

print(x1)

if x1:
  print("Yes, there is at least one match!")
else:
  print("No match")







#   \b

txt2 = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x2 = re.findall(r"ain\b", txt2)

print(x2)

if x2:
  print("Yes, there is at least one match!")
else:
  print("No match")









#   \B


txt3 = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x3 = re.findall(r"\Bain", txt3)

print(x3)

if x3:
  print("Yes, there is at least one match!")
else:
  print("No match")









#   \d

txt4 = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x4 = re.findall("\d", txt4)

print(x4)

if x4:
  print("Yes, there is at least one match!")
else:
  print("No match")








#   \D


txt5 = "The rain in Spain"

#Return a match at every no-digit character:

x5 = re.findall("\D", txt5)

print(x5)

if x5:
  print("Yes, there is at least one match!")
else:
  print("No match")








#   \s


txt6 = "The rain in Spain"

#Return a match at every white-space character:

x6 = re.findall("\s", txt6)

print(x6)

if x6:
  print("Yes, there is at least one match!")
else:
  print("No match")









#   \S


txt7 = "The rain in Spain"

#Return a match at every NON white-space character:

x7 = re.findall("\S", txt7)

print(x7)

if x7:
  print("Yes, there is at least one match!")
else:
  print("No match")








#   \w


txt8 = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x8 = re.findall("\w", txt8)

print(x8)

if x8:
  print("Yes, there is at least one match!")
else:
  print("No match")






#   \W



txt9 = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x9 = re.findall("\W", txt9)

print(x9)

if x9:
  print("Yes, there is at least one match!")
else:
  print("No match")









#   \Z


txt0 = "The rain in Spain"

#Check if the string ends with "Spain":

x0 = re.findall("Spain\Z", txt0)

print(x0)

if x0:
  print("Yes, there is a match!")
else:
  print("No match")

