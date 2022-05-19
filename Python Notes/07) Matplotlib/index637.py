import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y, height = 0.1)
plt.show()




#Bar Height
#The barh() takes the keyword argument height to set the height of the bars:
#
#Example
#Draw 4 very thin bars:
#
#
#The default height value is 0.8
