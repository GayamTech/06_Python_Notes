#  What is Train

import numpy
import matplotlib.pyplot as plt
numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

plt.scatter(x, y)
plt.show()


#  *** The x axis represents the number of minutes before making a purchase.

#  ** The y axis represents the amount of money spent on the purchase.

#  Test
#  Train/Test is a method to measure the accuracy of your model.

#  It is called Train/Test because you split the the data set into two sets: a training set and a testing set.

#  80% for training, and 20% for testing.

#  You train the model using the training set.

#  You test the model using the testing set.

#  Train the model means create the model.

#  Test the model means test the accuracy of the model.