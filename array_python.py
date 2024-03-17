#this page shows you how to use LISTS as ARRAYS, however, to work with arrays in python you will have to import a library, like the NumPy library
#arrays are used to store multiple values in one single variable

cars = ["Ford", "volvo", "bmw"]
x = cars[0]
print(cars)
print(x)
y = len(cars)
print(y)

cars.append("Honda")
#cars.pop(1)
cars.remove("volvo")
# cars should be no volvo and bmw become [1] honda is the last
print(cars)