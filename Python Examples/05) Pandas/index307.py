import pandas as pd

df = pd.read_csv('data2.csv')

df.fillna(130, inplace = True)

print(df.to_string())

#Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).














# Replace Empty Values
# Another way of dealing with empty cells is to insert a new value instead.

# This way you do not have to delete entire rows just because of some empty cells.

# The fillna() method allows us to replace empty cells with a value:

# Example
# Replace NULL values with the number 130: