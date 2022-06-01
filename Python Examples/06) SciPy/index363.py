from scipy.spatial.distance import hamming

p1 = (True, False, True)
p2 = (False, True, True)

res = hamming(p1, p2)

print(res)












# Hamming Distance


# Is the proportion of bits where two bits are difference.

# It's a way to measure distance for binary sequences.

# Example
# Find the hamming distance between given points: