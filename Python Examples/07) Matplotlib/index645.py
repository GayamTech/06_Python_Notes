import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()







#Colors
#You can set the color of each wedge with the colors parameter.
#
#The colors parameter, if specified, must be an array with one value for each wedge:
#
#Example
#Specify a new color for each wedge:


#You can use Hexadecimal color values, any of the 140 supported color names, or one of these shortcuts:
#
#'r' - Red
#'g' - Green
#'b' - Blue
#'c' - Cyan
#'m' - Magenta
#'y' - Yellow
#'k' - Black
#'w' - White
