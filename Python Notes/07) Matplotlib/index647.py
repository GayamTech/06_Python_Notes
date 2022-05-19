import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show()






#Legend With Header
#To add a header to the legend, add the title parameter to the legend function.
#
#Example
#Add a legend with a header:
