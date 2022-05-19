import numpy
from sklearn.metrics import r2_score
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))

print(r2)




#  **** Note: The result 0.799 shows that there is a OK relationship.

#R2
#Remember R2, also known as R-squared?
#
#It measures the relationship between the x axis and the y axis, and the value ranges from 0 to 1, where 0 means no relationship, and 1 means totally related.
#
#The sklearn module has a method called r2_score() that will help us find this relationship.
#
#In this case we would like to measure the relationship between the minutes a customer stays in the shop and how much money they spend.
#
#Example
#How well does my training data fit in a polynomial regression?
#
