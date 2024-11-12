first_set = {"apple", "banana", "cherry"}
#sets used to store multiple items in a single variable
#set is one of 4 built in data types in python used to store collection of data, the other 3 are list tuple and dictionary all with different qualities and usage
#a set is a collection which unordered unchangeable*, and unindexed
#set items are unchangeable, but you can remove items and add new items
#sets are written with curly brackets

print(first_set)

#set items are unordered, unchangeable and od not allow duplicate value

#unordred means that the items in a set do not have a defined order
#set items can appear in a different order every time you use them, and cannot be referred to by index or key.
#unchangeable: set items are unchangeable, meaning that we cannot change the item after the set has been created.
#once a set is created, you cannot change its items but you can remove itemsand add new items.
#duplicates重复 not allowed: sets cannot have two items with same value

second_set = {"apple", "banana", "cherry", True, 1, 2}
print(second_set)

third_set = {"apple", "banana", "cherry", False, True, 0}
print(third_set)

forth_set = {"apple", "banana", "cherry", "apple"}
print(forth_set)
print(len(forth_set))

#type()
#from python's perspective, sets are definied as objects with the data type "set"
print(type(first_set))

#the set() constructor构造函数 use it to make a set
#it is also possible to use the set() constructor to make a set
fifth_set = set(("apple", "banana", "cherry"))
print(fifth_set)

#python collection:

#list: is a collection which is ordered and changeable, allow duplicate members
#tuple: is a collection whcih is ordered and unchangeable, allows duplicate members
#set: is a collection which is unordered, unchangeable*, and unidexed.bo duplicate member
#dictionary: is a collection which ordered** and changeable, no duplicate member.

this_set = {"apple", "banana", "cherry"}

for x in first_set:
    print(x)

#once a set is created, you cannot change its items, but you can add new items.
#to add one item to a set use the add() method

first_set = {"apple", "banana", "cherry"}
first_set.add("orange")
print(first_set)

#to add items from another set into the current set, use the update() method
#add elements from tropical into first_set

tropical = {"pineapple", "mango", "papaya"}

first_set.update(tropical)
print(first_set)

#add any iterable

sixth_set = {"kiwi", "orange"}
first_set.update(sixth_set)
print(first_set)

#remove item

first_set.remove("banana")
print(first_set)

#discard method can avoid rasing error
#you can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that get removed
#the return value of pop()method is the removd item
#You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
#the return value of the pop() method is the removed item.

x = first_set.pop()
print(x)
print(first_set)

#clear method is used to umpitise the set
#del keyword will delete the set completely

#loop sets
#you can loop thourgh the set items by using a for loop:

this_set = {"apple", "banana", "cherry"}

[x for x in this_set]
print(x)
print(this_set)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

#the union()menthod returns a new set with all items from both sets
#the update() method insets 
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)

#keep only the duplicate
#the intersection_update() method willkeep only the items that are present in both sets
#it used to find common element in both two sets
set_x = {"apple", "banana","cherry"}
set_y = {"google", "microsoft", "apple"}
set_x.intersection_update(set_y)
print(set_x)

set_z = set_x.intersection(set_y)
print(set_z)

#keep all but not the duplicates\\
#the symmetric_difference_update() method will keep only the element that are not present in both sets

set_x.symmetric_difference_update(set_y)
print(set_x)
"""add(): add and elements to the set
   clear(): removes all the elements from the set
   copy(): return a copy of the set
   difference(): return a set containing the difference between 2 or more sets
   difference_update(): removes the items in this set that are also included in another specified set
   discard(): remove the specified item
   intersection(): return a set that is the intersection of 2 other set
   intersection_update(): removes the item in this set that are not present in other, specified sets
   isdisjoint(): return whether 2 sets have a intersection or not 
   issubset(): return whether another set contain this set or not
   issuperset(): return whether this set contain another set or not
   pop(): removes an element from set
   remove(): remove the specified element
   symmetric_difference(): return a set with the symmetric difference of 2 sets
   symmetric_difference_update(): inserts the symmetric difference from this set and another
   union():return a set containing the union of set
   update():update the set with the union of this set and others
"""

