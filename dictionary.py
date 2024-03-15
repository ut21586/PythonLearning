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

#removing items
#pop() method removes the item with the specified key name
first_dict.pop("model")
print(first_dict)

first_dict.popitem() #popitem could be remove last item
print(first_dict)

#loop dictionaries
for x in first_dict.values():
    print(x)

for x, y in first_dict.items():
    print(x, y)

#copy dictionary
#cannot copy dictionary simply by typing dict2=dict1, because: dict2 will only be a reference to dict1 and changes made in dict1
#will automatically also be made in dict2 

first_dict = second_dict.copy()
print(first_dict)
print(second_dict)
third_dict = dict(first_dict)
print(third_dict)

#python -nested directionaries: a directionary can contain directionries, this is called nested directioneries
his_family = {
    "child1": {
        "name": "Email",
        "year": 2004
    },
    "child2": {
        "name": "tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2001
    }
}
print(his_family["child2"]["name"])

""" 
clear(): removes all the elements from the dictonary
copy(): returns a copy of dictionary
fromkeys(): returns a dictionary with the specified keys and value
get(): returns thevalue pf the specified key
items(): returns a list containing a tuple for each key value pair
keys(): returns a list containing the dictionary's key
pop(): removes the element with specified key
popitem():removes the last inserted key-value pair
setdefault(): returns the valeu of the specified key if the key does not exist: insert the key with the specifed value
update(): updates the dictionary with the specified key-value pairs
values():returns a list of all the values in the dictonary
"""