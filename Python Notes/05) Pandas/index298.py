import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df)







# In my system the number is 60, which means that if the DataFrame contains more than 60 rows, the print(df) statement will return only the headers and the first and last 5 rows.

# You can change the maximum rows number with the same statement.

# Example
# Increase the maximum number of rows to display the entire DataFrame:
