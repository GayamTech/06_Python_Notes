import pandas
from sklearn import linear_model

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

predictedCO2 = regr.predict([[3300, 1300]])

print(predictedCO2)


#  We have already predicted that if a car with a 1300cm3 engine weighs 2300kg, the CO2 emission will be approximately 107g.

#  What if we increase the weight with 1000kg?

#  Example
#  Copy the example from before, but change the weight from 2300 to 3300:
    
    
    
#  We have predicted that a car with 1.3 liter engine, and a weight of 3300 kg, will release approximately 115 grams of CO2 for every kilometer it drives.

#  Which shows that the coefficient of 0.00755095 is correct:

#  107.2087328 + (1000 * 0.00755095) = 114.75968