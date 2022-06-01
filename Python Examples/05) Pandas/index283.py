import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar[0])






# Labels
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.

# This label can be used to access a specified value.

# Example
# Return the first value of the Series:
