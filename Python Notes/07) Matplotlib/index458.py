import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()






# ColorMap

# The Matplotlib module has a number of available colormaps.

# A colormap is like a list of colors, where each color has a value that ranges from 0 to 100.

# Here is an example of a colormap:

# This colormap is called 'viridis' and as you can see it ranges from 0, which is a purple color, and up to 100, which is a yellow color.

# How to Use the ColorMap
# You can specify the colormap with the keyword argument cmap with the value of the colormap, in this case 'viridis' which is one of the built-in colormaps available in Matplotlib.

# In addition you have to create an array with values (from 0 to 100), one value for each of the point in the scatter plot:









# Example
# Create a color array, and specify a colormap in the scatter plot: