

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression

# The expression is executed and the result is returned:





# Add 10 to argument a, and return the result:

print(" ")

x = lambda a: a + 10
print(x(5))








# Lambda functions can take any number of arguments:

# Multiply argument a with argument b and return the result:



print(" ")


y = lambda c, b: c * b
print(y(5, 6))











# Summarize argument a, b, and c and return the result:

print(" ")


z = lambda d, e, f: d + e + f
print(z(5, 6, 2))











# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# def myfunc(n):
#  return lambda a : a * n

# Use that function definition to make a function that always doubles the number you send in:



print(" ")



def myfunc(n):
  return lambda g : g * n

mydoubler = myfunc(2)

print(mydoubler(11))














# Or, use the same function definition to make a function that always triples the number you send in:


print(" ")


def myfunc1(n):
  return lambda h : h * n

mytripler = myfunc1(3)

print(mytripler(11))















# Or, use the same function definition to make both functions, in the same program:

# Use lambda functions when an anonymous function is required for a short period of time.


print(" ")



def myfunc2(n):
  return lambda i : i * n

mydoubler1 = myfunc2(2)
mytripler1 = myfunc2(3)

print(mydoubler1(11))
print(mytripler1(11))

print(" ")