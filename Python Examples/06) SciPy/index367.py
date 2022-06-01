from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

#Export:
io.savemat('arr.mat', {"vec": arr})

#Import:
mydata = io.loadmat('arr.mat', squeeze_me=True)

print(mydata['vec'])










# In order to resolve this we can pass an additional argument squeeze_me=True:

# Example


