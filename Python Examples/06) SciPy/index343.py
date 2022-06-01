from scipy.optimize import root
from math import cos

def eqn(x):
  return x + cos(x)

myroot = root(eqn, 0)

print(myroot)





# Example

# Print all information about the solution (not just x which is the root)

