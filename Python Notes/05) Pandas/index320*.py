#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot()

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()









# Pandas - Plotting




# Plotting
# Pandas uses the plot() method to create diagrams.

# We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen.

# Read more about Matplotlib in our Matplotlib Tutorial.

# Example
# Import pyplot from Matplotlib and visualize our DataFrame:








# The examples in this page uses a CSV file called: 'data.csv'.

