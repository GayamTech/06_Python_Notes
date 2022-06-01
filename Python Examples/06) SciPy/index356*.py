import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 0, 1],
  [1, 1, 1, 1],
  [2, 1, 1, 0],
  [0, 1, 0, 1]
])

newarr = csr_matrix(arr)

print(breadth_first_order(newarr, 1))










# Breadth First Order


# The breadth_first_order() method returns a breadth first traversal from a node.

# This function takes following arguments:

# the graph.
# the starting element to traverse graph from.
# Example
# Traverse the graph breadth first for given adjacency matrix:

