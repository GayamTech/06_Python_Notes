import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()







# Compare Plots

# In the example above, there seems to be a relationship between speed and age, but what if we plot the observations from another day as well? Will the scatter plot tell us something else?





# Example
# Draw two plots on the same figure:



# Note: The two plots are plotted with two different colors, by default blue and orange, you will learn how to change colors later in this chapter.





# By comparing the two plots, I think it is safe to say that they both gives us the same conclusion: the newer the car, the faster it drives.

