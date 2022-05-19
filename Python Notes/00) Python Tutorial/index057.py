
# Python Classes and Objects




# Python Classes/Objects
# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
# To create a class, use the keyword class:

# Example
# Create a class named MyClass, with a property named x:



print(" ")

class MyClass:
  x = 5

print(MyClass)













# Create Object
# Now we can use the class named MyClass to create objects:

# Create an object named p1, and print the value of x:

print(" ")

class MyClass1:
  y = 5

p1 = MyClass1()
print(p1.y)










# The __init__() Function
# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function to assign values for name and age:

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

print(" ")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)


















# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:

# Insert a function that prints a greeting, and execute it on the p1 object:


# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


print(" ")

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p3 = Person1("John", 36)
p3.myfunc()









# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:


print(" ")

class Person2:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p4 = Person2("John", 36)
p4.myfunc()
















# Modify Object Properties
# You can modify properties on objects like this:

# Set the age of p1 to 40:

print(" ")


class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p5 = Person3("John", 36)

p5.age = 40

print(p5.age)
















# Delete Object Properties
# You can delete properties on objects by using the del keyword:

# Delete the age property from the p1 object:

print(" ")


class Person4:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p6 = Person4("John", 36)

del p6.age


#  print(p6.age)



















# Delete Objects
# You can delete objects by using the del keyword:

# Delete the p1 object:

print(" ")

class Person5:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p7 = Person5("John", 36)

del p7


#  print(p7)













# The pass Statement

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

print(" ")


class Person:
  pass


print(" ")
# having an empty class definition like this, would raise an error without the pass statement
