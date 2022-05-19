import pandas as pd

df = pd.read_csv('data2.csv')

for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

print(df.to_string())











# For small data sets you might be able to replace the wrong data one by one, but not for big data sets.

# To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries.

# Example
# Loop through all values in the "Duration" column.

# If the value is higher than 120, set it to 120: