import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))

plt.scatter(x, y, c=colors, cmap='gist_ncar_r')

plt.colorbar()

plt.show()

