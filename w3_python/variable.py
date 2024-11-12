# declare variables.

x = 5
y = "whats going on?"
x = str(3) #string
x = int(3) #integer
x = float(3) #float number

print(x) # print value of x
print(type(x)) #print var type of x
print(y)

#camel case: each first letter name is captital except first
#pascal case : every words first are capital my prefer!
#snake case: there is "_" between each word instead of space

#assign mnultiple variable:

x, y, z = "First", "Second", "Third"

x = y = z = "Orange" #exp for 1 value but multi-variables

# extract multiple-values into multiple variable:
fruits = ["apple", "banana", "orange"]
x, y, z = fruits

m = "python is awsome"

print(m)

a = "python "
b = "is "
c = "awsome"

print(a, b, c)
print(a +b + c)


#global variable : variables created outside of the function but it can be used by the inside and outside of the function
#create a variable outside of a funciton and print it at inside of the function

x = "awsome"

def myfunc(): 
              y = "hello world"
              z = "java?nope its python"
              print("Python is" + x)
            
myfunc()

#if you create a var with same name of the fucntion which means
#this var is local var and only be used inside of the function
# exp:

x = "awsome"

def youfunc(): 
               x = "fantastic"
               print("Python is " + x)

youfunc()

print("Python is" + x)



#global key word
x = "awsomw"
def itfunc(): 
              global x
              x ="fantastic"
itfunc()
print("Python is " + x)
             
 