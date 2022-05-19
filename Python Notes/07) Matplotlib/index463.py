import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, cmap='Blues_r')

plt.colorbar()

plt.show()







# Blues_r
    
# Available ColorMaps
# You can choose any of the built-in colormaps:

