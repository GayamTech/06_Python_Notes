import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df.loc["day2"])






# Locate Named Indexes

# Use the named index in the loc attribute to return the specified row(s).

# Example
# Return "day2":
