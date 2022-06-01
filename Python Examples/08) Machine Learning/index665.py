from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
  return slope * x + intercept

speed = myfunc(10)

print(speed)







#  Predict Future Values
#   Now we can use the information we have gathered to predict future values.

#   Example: Let us try to predict the speed of a 10 years old car.

#  To do so, we need the same myfunc() function from the example above:

#   def myfunc(x):
#     return slope * x + intercept

#  Example
#  Predict the speed of a 10 years old car:

