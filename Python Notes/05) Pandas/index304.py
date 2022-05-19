import pandas as pd

df = pd.read_csv('data.csv')

print(df.info())






# Info About the Data
# The DataFrames object has a method called info(), that gives you more information about the data set.

# Example
# Print information about the data:

# Result Explained
# The result tells us there are 169 rows and 4 columns:


#   RangeIndex: 169 entries, 0 to 168
#   Data columns (total 4 columns):

# And the name of each column, with the data type:


#    #   Column    Non-Null Count  Dtype  
#   ---  ------    --------------  -----  
#    0   Duration  169 non-null    int64  
#    1   Pulse     169 non-null    int64  
#    2   Maxpulse  169 non-null    int64  
#    3   Calories  164 non-null    float64

# Null Values
# The info() method also tells us how many Non-Null values there are present in each column, and in our data set it seems like there are 164 of 169 Non-Null values in the "Calories" column.

# Which means that there are 5 rows with no value at all, in the "Calories" column, for whatever reason.

# Empty values, or Null values, can be bad when analyzing data, and you should consider removing rows with empty values. This is a step towards what is called cleaning data, and you will learn more about that in the next chapters.
