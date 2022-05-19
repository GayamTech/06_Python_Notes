# Elif

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".


print(" ")

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")








# Else

# The else keyword catches anything which isn't caught by the preceding conditions.

print(" ")

c = 200
d = 33
if d > c:
  print("b is greater than a")
elif d == c:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
  
  










# You can also have an else without the elif:

# Example

print(" ")


e = 200
f = 33
if f > e:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
# Short Hand If
# If you have only one statement to execute, you can put it on the same line as the if statement.

# One line if statement:

print(" ")
  
g = 200
h = 33

if g > h: print("a is greater than b")

  
  
  













# Short Hand If ... Else

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

# One line if else statement:

# This technique is known as Ternary Operators, or Conditional Expressions.

print(" ")

i = 2
j = 330

# print("A") if i > j else print("B")














# You can also have multiple else statements on the same line:

# One line if else statement, with 3 conditions:


print(" ")

k = 330
l = 330
# print("A") if k > l else print("=") if k == l else print("B")
















# And
# The and keyword is a logical operator, and is used to combine conditional statements:

# Test if a is greater than b, AND if c is greater than a:


print(" ")

m = 200
n = 33
o = 500
if m > n and o > m:
  print("Both conditions are True")
  
  
  
  
  
  
  
  
  
  
  


# Or
# The or keyword is a logical operator, and is used to combine conditional statements:

# Test if a is greater than b, OR if a is greater than c:

print(" ")

p = 200
q = 33
r = 500
if p > q or p > r:
  print("At least one of the conditions is True")
  
  
  
  
  
  
  
  
  
  
  
  
  
# Nested If
# You can have if statements inside if statements, this is called nested if statements.

print(" ")

s = 41

if s > 10:
  print("Above ten,")
  if s > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")













# The pass Statement

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

print(" ")

t = 33
u = 200

if u > t:
  pass

# having an empty if statement like this, would raise an error without the pass statement

print(" ")