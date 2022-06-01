import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

mat = csr_matrix(arr)
mat.sum_duplicates()

print(mat)











# Eliminating duplicate entries with the sum_duplicates() method:




# Example
# Eliminating duplicates by adding them: