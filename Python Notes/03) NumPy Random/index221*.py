from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False)

plt.show()





# Visualization of Zipf Distribution
# Sample 1000 points but plotting only ones with value < 10 for more meaningful chart.

# Example

