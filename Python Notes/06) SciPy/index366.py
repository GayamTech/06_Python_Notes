from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

#Export:
io.savemat('arr.mat', {"vec": arr})

#Import:
mydata = io.loadmat('arr.mat')

print(mydata['vec'])







# Use the variable name "vec" to display only the array from the matlab data:

# Example








# Note: We can see that the array originally was 1D, but on extraction it has increased one dimension.

