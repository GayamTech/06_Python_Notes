from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))

print(x)





# Even if you run the example above 100 times, the value 9 will never occur.

# You can return arrays of any shape and size by specifying the shape in the size parameter.

# Example
# Same example as above, but return a 2-D array with 3 rows, each containing 5 values.
