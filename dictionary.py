#dictionaries are used to store data values in key: value pairs
#a dictionary is a collection which is ordered, changeable and do not allow duplicate
#dictionaries are written with curly brackets and have keys and values

first_dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(first_dict)
print(first_dict["brand"])

#dictionary length is used to determine how many items a dictionary has use len() function
print(len(first_dict))
print(type(first_dict))
#it is also possible to used the dict() constructor to make a dictionary
second_dict = dict(name = "john", age = 36, country = "norway")
print(second_dict)
x = second_dict["age"] # x now equal to 36
#also can use get method to achieve above action
#keys() method will return a list of all keys in the dictionary
x = second_dict.keys()
print(x)
second_dict["color"] = "white"
print(x)

x = second_dict.values()
print(x)


#get items, use items() method will return each item in a dictionary, as tuples in a list.
x = second_dict.items()
print(x)

#check if key exist: use "in" keyword
check = ["yes" if "model" in first_dict else "no"]
print(check)

#change dictionary items
first_dict["car"] = "tesla"
#first_dict["version"] = "tesla"
first_dict.update({"version": "modelx"})
print(first_dict)