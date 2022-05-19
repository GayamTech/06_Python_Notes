import pandas as pd

df = pd.read_csv('data2.csv')

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68












# Replace Using Mean, Median, or Mode
# A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

# Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:

# Example
# Calculate the MEAN, and replace any empty values with it:








# Mean = the average value (the sum of all values divided by number of values).