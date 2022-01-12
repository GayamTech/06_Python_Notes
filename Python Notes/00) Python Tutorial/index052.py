# Python Loops
# Python has two primitive loop commands:

# while loops
# for loops


# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.

# Example
# Print i as long as i is less than 6:


# Note: remember to increment i, or else the loop will continue forever.



i = 1
while i < 6:
  print(i)
  i += 1













# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

# Exit the loop when i is 3:




j = 1
while j < 6:
  print(j)
  if (j == 3):
    break
  j += 1









# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

# Continue to the next iteration if i is 3:


k = 0
while k < 6:
  k += 1
  if k == 3:
    continue
  print(k)

# Note that number 3 is missing in the result










# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

# Print a message once the condition is false:


l = 1
while l < 6:
  print(l)
  l += 1
else:
  print("i is no longer less than 6")










