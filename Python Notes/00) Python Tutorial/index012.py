# Python Numbers

# There are three numeric types in Python:    int   ,  float  ,   complex


print("")

x = 1    # int
y = 2.8  # float
z = 1j   # complex


print(type(x))
print(type(y))
print(type(z))
print("")





# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited
# length.




a = 1
b = 35656222554887711
c = -3255522

print(type(a))
print(type(b))
print(type(c))
print("")


# Float, or "floating point number" is a number, positive or negative, containing one or
# more decimals.




d = 1.10
e = 1.0
f = -35.59

print(type(d))
print(type(e))
print(type(f))
print("")



# Float can also be scientific numbers with an "e" to indicate the power of 10.


g = 35e3
h = 12E4
i = -87.7e100

print(g)
print(h)
print(i)
print(type(g))
print(type(h))
print(type(i))
print("")



# Complex numbers are written with a "j" as the imaginary part




j = 3+5j
k = 5j
l = -5j

print(type(j))
print(type(k))
print(type(l))
print("")






# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods





m = 1    # int
n = 2.8  # float
o = 1j   # complex

#convert from int to float:
p = float(m)

#convert from float to int:
q = int(n)

#convert from int to complex:
r = complex(o)

print(p)
print(q)
print(r)
print("")
print(type(p))
print(type(q))
print(type(r))
print("")


# Note: You cannot convert complex numbers into another number type.








