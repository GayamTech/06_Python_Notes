import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, cmap='BuGn_r')

plt.colorbar()

plt.show()












#BuGn_r
    
    
    
# Available ColorMaps
# You can choose any of the built-in colormaps: