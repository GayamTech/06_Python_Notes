from scipy.optimize import minimize

def eqn(x):
  return x**2 + x + 2

mymin = minimize(eqn, 0, method='BFGS')

print(mymin)











# Minimizing a Function
# A function, in this context, represents a curve, curves have high points and low points.

# High points are called maxima.

# Low points are called minima.

# The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima.

# The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.

# Finding Minima
# We can use scipy.optimize.minimize() function to minimize the function.

# The minimize() function takes the following arguments:

# fun - a function representing an equation.

# x0 - an initial guess for the root.

# method - name of the method to use. Legal values:
#     'CG'
#     'BFGS'
#     'Newton-CG'
#     'L-BFGS-B'
#     'TNC'
#     'COBYLA'
#     'SLSQP'

# callback - function called after each iteration of optimization.

# options - a dictionary defining extra params:

# {
#      "disp": boolean - print detailed description
#      "gtol": number - the tolerance of the error
#   }






# Example
# Minimize the function x^2 + x + 2 with BFGS:

