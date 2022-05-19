import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show()







#Legend
#To add a list of explanation for each wedge, use the legend() function:
#
#Example
#Add a legend:
