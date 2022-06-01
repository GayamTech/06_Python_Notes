import pandas as pd

df = pd.read_csv('data2.csv')

df.dropna(inplace = True)

print(df.to_string())

#Notice in the result that some rows have been removed (row 18, 22 and 28).

#These rows had cells with empty values.







# If you want to change the original DataFrame, use the inplace = True argument:

# Example
# Remove all rows with NULL values:






# Note: Now, the dropna(inplace = True) will NOT return a new DataFrame, but it will remove all rows containg NULL values from the original DataFrame.