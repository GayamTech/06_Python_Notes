import numpy as np
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(depth_first_order(newarr, 1))









# Depth First Order
# The depth_first_order() method returns a depth first traversal from a node.

# This function takes following arguments:

# the graph.
# the starting element to traverse graph from.




# Example
# Traverse the graph depth first for given adjacency matrix: