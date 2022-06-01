# Python Booleans

print("")
print(10 > 9)
print(10 == 9)
print(10 < 9)


print("")



a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
print("")
  
  
  


print(bool("Hello"))
print(bool(15))
print(bool(0))


print("")




x = "Hello"
y = 15

print(bool(x))
print(bool(y))





print("")


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))






print("")


print("Examples of False Bools: False, None, 0, "", (), [], {}")



print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))





print("")






class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))






print("")







def myFunction() :
  return True

print(myFunction())






print("")






def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")









print("")




x = 200
print(isinstance(x, int))


print("")
