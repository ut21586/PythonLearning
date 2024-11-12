# python si an objecy oriented programming language.
#almost everything in python is an object, with its properties and methods.
#a class is like an object constructor or a "blueprint" for creating objects.

class first_class:
    x = 5
    print(x)

p1 = first_class()
print(p1.x)

#the_init()Function
#the examples above are classes and objects in their simplest form, and are not really useful in real life applications
#to undertand the meaning of classes we have to understand the built-in_init_()function
#All classes have a funcrion called _init_() which is always executed when the class is being initiated
#use the_init_()function to assign values to object properties, or other operations that are necessary to do when object is being created：

#create a class named Person, use the_init_()function to assign value for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("john", 36)

print(p1.name)
print(p1.age)


#The__str__()function: controls what should be returned when the class object is represented as a string
#If the__str__()function is not set, the string representation of the object is returned:
class Person:
    def __init__(self, name, age):
     self.name = name 
     self.age = age

p1 = Person("John", 36)
print(p1)

#object Method
#object can also contain methods. methods in objects are functions that belong to the object.
#insert a function that prints a greeting,and executed it on the p1 object:

class People:
   def __init__(self, name, age):
      self.name = name
      self.age = age 

   def myfunc(self):
      print("Hello my name is" + self.name)

p1 = Person("John", 36)
#p1.Child()

#modify object properties

#python inheritance 继承
"""
parent class: is the class being inherited from, also called base class
child class: is the class that inherits from another class also called derived class
"""

#create a Parent class
class Parent:
   def __init__(self, fname, lname):
      self.firstname = fname
      self.lastname = lname

   def printname(self):
      print(self.firstname, self.lastname)

#use the person class tpo create an object, and thn execute the printname method:

x = Person("john", "Doe")
x.printname()

#create a child class
class Child(Parent):
   def __init__(self, fname, lname):
      Parent.__init__(self, fname, lname)
      #add properties etc.
      #from now children no longer inherit the parent's __init__() function
      # too keep

#add the __init__()Fucntion

#use super() Function: Python also has a super()function that will malke the child class inherit all the methods and properties from its parent:
class Child(Parent):
   def __init__(self, fname, lname, year):
      super().__init__(fname, lname)
      self.graduatonyear = year
#x = Child("Mike", "olsen", 2019)
   def welcome(self):
      print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
