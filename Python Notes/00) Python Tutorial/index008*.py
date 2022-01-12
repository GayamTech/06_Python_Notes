x, y, z = "Orange", "Banana", "Cherry"

print(x)
print(y)
print(z)



# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line
# Note: Make sure the number of variables matches the number of values, or else you will get an error.



# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:


a = b = c = "Orange"
print(a)
print(b)
print(c)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.



fruits = ["apple", "banana", "cherry"]
d, e, f = fruits
print(d)
print(e)
print(f)