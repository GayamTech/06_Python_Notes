import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()





# Matplotlib Scatter




# Creating Scatter Plots
# With Pyplot, you can use the scatter() function to draw a scatter plot.

# The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis, and one for values on the y-axis:



# Example
# A simple scatter plot:






# The observation in the example above is the result of 13 cars passing by.

# The X-axis shows how old the car is.

# The Y-axis shows the speed of the car when it passes.

# Are there any relationships between the observations?

# It seems that the newer the car, the faster it drives, but that could be a coincidence, after all we only registered 13 cars.

