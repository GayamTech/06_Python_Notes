import pandas
from sklearn import tree
import pydotplus
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import matplotlib.image as pltimg

df = pandas.read_csv("shows.csv")

d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)







#To make a decision tree, all data has to be numerical.
#
#We have to convert the non numerical columns 'Nationality' and 'Go' into numerical values.
#
#Pandas has a map() method that takes a dictionary with information on how to convert the values.
#
#{'UK': 0, 'USA': 1, 'N': 2}
#
#Means convert the values 'UK' to 0, 'USA' to 1, and 'N' to 2.
#
#Example
#Change string values into numerical values:
