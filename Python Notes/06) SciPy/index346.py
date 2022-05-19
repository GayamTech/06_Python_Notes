import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

print(csr_matrix(arr).data)







# Sparse Matrix Methods
# Viewing stored data (not the zero items) with the data property:

# Example