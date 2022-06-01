import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

plt.scatter(train_x, train_y)
plt.show()



#Display the same scatter plot with the training set:
#
#Example
#plt.scatter(train_x, train_y)
#plt.show()
#Result:
#It looks like the original data set, so it seems to be a fair selection:
#


#Split Into Train/Test
#The training set should be a random selection of 80% of the original data.
#
#The testing set should be the remaining 20%.
#
#train_x = x[:80]
#train_y = y[:80]
#
#test_x = x[80:]
#test_y = y[80:]
#
#Display the Training Set
#Display the same scatter plot with the training set:
#
