import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()




#Bar Width
#The bar() takes the keyword argument width to set the width of the bars:
#
#Example
#Draw 4 very thin bars:
#
#The default width value is 0.8
#
#Note: For horizontal bars, use height instead of width.
