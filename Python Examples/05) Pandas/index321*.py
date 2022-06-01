#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()








# Scatter Plot
# Specify that you want a scatter plot with the kind argument:

# kind = 'scatter'

# A scatter plot needs an x- and a y-axis.

# In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.

# Include the x and y arguments like this:

# x = 'Duration', y = 'Calories'







# Remember: In the previous example, we learned that the correlation between "Duration" and "Calories" was 0.922721, and we conluded with the fact that higher duration means more calories burned.

# By looking at the scatterplot, I will agree.