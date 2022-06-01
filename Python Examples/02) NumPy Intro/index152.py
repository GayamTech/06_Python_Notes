import numpy as np

arr = np.array([1, 2, 3])

for idx, x in np.ndenumerate(arr):
  print(idx, x)
  
  
  
  
  
# Enumerated Iteration Using ndenumerate()


# Enumeration means mentioning sequence number of somethings one by one.

# Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.

# Example
# Enumerate on following 1D arrays elements:
