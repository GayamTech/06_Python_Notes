import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()








# Multiple Lines
# You can plot as many lines as you like by simply adding more plt.plot() functions:





# Example
# Draw two lines by specifying a plt.plot() function for each line:







# You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

# (In the examples above we only specified the points on the y-axis, meaning that the points on the x-axis got the the default values (0, 1, 2, 3).)