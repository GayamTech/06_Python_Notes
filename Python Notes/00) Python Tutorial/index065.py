# Using the dir() Function

# There is a built-in function to list all the function names (or variable names) in a module. The dir() function:





# Example

# List all the defined names belonging to the platform module:




# Note: The dir() function can be used on all modules, also the ones you create yourself.



import platform


print(" ")


x = dir(platform)

print(x)


print(" ")