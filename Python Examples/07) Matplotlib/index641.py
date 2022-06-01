import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()







#Labels
#Add labels to the pie chart with the label parameter.
#
#The label parameter must be an array with one label for each wedge:
#
#Example
#A simple pie chart:
