#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()








#Start Angle
#As mentioned the default start angle is at the x-axis, but you can change the start angle by specifying a startangle parameter.
#
#The startangle parameter is defined with an angle in degrees, default angle is 0:
#
#
#
#
#Example
#Start the first wedge at 90 degrees:
