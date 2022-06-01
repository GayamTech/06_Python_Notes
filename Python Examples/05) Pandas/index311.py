import pandas as pd

df = pd.read_csv('data2.csv')

x = df["Calories"].mode()[0]

df["Calories"].fillna(x, inplace = True)

print(df.to_string())

#As you can see in row 18 and 28, the empty value from "Calories" was replaced with the mode: 300.0














# Example
# Calculate the MODE, and replace any empty values with it:




# Mode = the value that appears most frequently.