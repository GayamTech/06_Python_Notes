from scipy.spatial.distance import euclidean

p1 = (1, 0)
p2 = (10, 2)

res = euclidean(p1, p2)

print(res)













# Distance Matrix
# There are many Distance Metrics used to find various types of distances between two points in data science, Euclidean distsance, cosine distsance etc.

# The distance between two vectors may not only be the length of straight line between them, it can also be the angle between them from origin, or number of unit steps required etc.

# Many of the Machine Learning algorithm's performance depends greatly on distance metrices. E.g. "K Nearest Neighbors", or "K Means" etc.

# Let us look at some of the Distance Metrices:

# Euclidean Distance
# Find the euclidean distance between given points.

# Example