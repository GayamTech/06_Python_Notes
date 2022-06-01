from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

#Export:
io.savemat('arr.mat', {"vec": arr})

#Import:
mydata = io.loadmat('arr.mat')

print(mydata)








# Import Data from Matlab Format
# The loadmat() function allows us to import data from a Matlab file.

# The function takes one required parameter:

# filename - the file name of the saved data.

# It will return a structured array whose keys are the variable names, and the corresponding values are the variable values.




# Example
# Import the array from following mat file.: