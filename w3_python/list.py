#extend() used to append element to current list from another list
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#print(thislist.extend(tropical))

thistuple=("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
thislist.remove("banana")
print(thislist)
second_list = ["apple", "banana","orange", "banana", "cherry", "kiwi"]
second_list.remove("banana") #default that remove first target in list
print(second_list) 
second_list.pop(1) #delete "orange"
print(second_list)
second_list.pop() #delete last item in list:"kiwi"
print(second_list)
del second_list[1]
print(second_list)
del second_list
del thislist
del thistuple

#until now, deleted all list, none of available list

first_list = ["apple", "orange", "banana", "cherry", "kiwi"]
print(first_list)
first_list.clear() 
print(first_list)

#loop list
third_list = ["apple", "banana","cherry","kiwi", "mango"]
[print(x) for x in third_list]


#list comprehension

# new_list = []

# for x in third_list:
#     if "a" in x:
#         new_list.append(x)

new_list = [x for x in third_list if "a" in x]
print(new_list)
new_list = [x for x in range(10) if x < 5] #filter if 
print(new_list)
new_list = [x.upper() for x in third_list]
print(new_list)
new_list = ["hello" for x in third_list]
print(new_list)
new_list = [x if x != "banana" else "orange" for x in third_list] #expression
print(new_list)

