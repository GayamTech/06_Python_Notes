import pandas as pd

df = pd.read_csv('data2.csv')

x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the median: 291.2












# Example
# Calculate the MEDIAN, and replace any empty values with it:




# Median = the value in the middle, after you have sorted all values ascending.