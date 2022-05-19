#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df["Duration"].plot(kind = 'hist')

plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()








# Histogram
# Use the kind argument to specify that you want a histogram:

# kind = 'hist'

# A histogram needs only one column.

# A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?

# In the example below we will use the "Duration" column to create the histogram:



# Note: The histogram tells us that there were over 100 workouts that lasted between 50 and 60 minutes.