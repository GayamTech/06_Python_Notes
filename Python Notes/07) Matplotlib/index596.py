import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, cmap='prism')

plt.colorbar()

plt.show()





# PuBuGn




# Available ColorMaps
# You can choose any of the built-in colormaps:
