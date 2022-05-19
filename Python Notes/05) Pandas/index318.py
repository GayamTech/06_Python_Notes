import pandas as pd

df = pd.read_csv('data2.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())

#Notice that row 12 has been removed from the result











# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.

# Example
# Remove all duplicates:



# Remember: The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.