# Here, first import the math module



# Write a function to do the following
# Input: area of circle
# Output: radius of circle


# Write a function to compute factorial
# Input: n
# Output: the factorial of n



# Do this after you learn list
# Write a function to compute dot product of two vectors represeted with list 
# Input: two vectors in list 
# Output: dot product of the two vectors



# Write a function to compute the sin(2 * theta) + cos(3 * theta - pi / 3) + exp(2 * x)
# Input: theta, x
# Output: function value 


# f-string faster than normal string encoding way
# exp: greeting = f"Hello, {name}!
# 
# \' single quote
# \\ backslash
# \n new line
# \r carriage return
# \t tab
# \b backspace
# \f form feed
# \ooo octal value
# \xhh hex value


# capitalize(): convert the first character to upper case
# casefold(): convert string into lower case
# center(): returns a centered string
# count(): returns the number of times a specified 
# encode(): return teh encode version fo the string
# endswith(): returns true if the string end with specific values
# expandtabs(): sets the tab of the string
# find(): searchs the string for a specofoed value and returns the position of where it was found
# format(): formats specified values in a string
# format_map(): formats specified values in a string used useful when you have the dictionary
# index(): search the string for a specified value and returns the position of where it was found
# isalnum(): return true if all characters in the string are alphanumeric
# isalpha(): return true if all characters in the string are ascii character
# isdecimal(): return true if all characters in the string are decimals
# isdigit(): returns true if all characters in the string are digits
#isidentifier(): return true if all teh string is an identifier
# islower(): return true if all characters in the string are lower case
# isnumeric(): returns true if all characters in the string are numeric 
# isprintable(): returnd true if all characters in teh string are printable
# isspace(): returnd true if all characters in the string are whitespaces
# istitle(): returns true if the string follows the rules of a title
# isupper(): returns true if all characters in the string are upper case
# join(): joins the elements of an iterable to end of the string
# ljust(): returns a left justified version of the string
# lower(): converts a string into lower case
# lstrip(): returns a left trim version of the string
# maketrans(): returns a translation table to be used in 
'''
TranslationTable = str.maketrans('abc', '123', 'c')
text = "abcde"
TranslatedText = text.translate(TranslationTable)
print(TranslationText)

vowels = "aeiou"
numbers = "12345"
RemoveChars = "xyz"
TranslationTable = str.maketrans(vowels, numbers, RemoveChars) # output should be 12345

text = "hello world, xyz!"
TranslatedText = text.translate(TranslationTable)
print(TranslatedText) # output should be h2114 w4rld
'''


# partitione(): return a tuple where the string is parted into three parts
# replace(): returns a string where a specified value is replaced with a specified value
# rfind(): searches the string for a specified value and returns the last postion of hwere it was found
# rindex(): searches the string for a specified value and returns the last position of where it found
# rjust(): returns a right justified version of the string
# rpartition(): returns a tuple where the string is parted into three parts unlike pertition() it split the string before the last element
# rsplit(): split the string ar the specified separator and return a list
# splitlines(): splits the string at line breaks and returns a list
# startswith(): returns true if the string starts with a specified value
# strip(): returns a trimmed 修剪 version o th string
# swapcase(): swaps cases lower case becomes upper case and vice versa
# title(): converts the first character of each word to upper   case
# translate(): returns a translated string
# upper(): converts a string into upper case
# zfill(): fills the string with a specified number of 0 values at the beginning


""" 
list is ordered and changeable also allow duplicate复制 members
"""


"""
remove function: just remove any item in the list
pop function:  remove the item with specified index, if () bracket empty default remove the last item
whats the differences between the pop and remove?: 

del means delete can both delete any item and whole list
Use clear can empty the whole list
"""

"""
SORT LIST

sort()
sort(reverse == True): sort descending
sort(key = function): teh function will return a number taht will be used to sort the list(the lowest number first)
"""

"""
DATA TYPE

text type: str
numeric type: int, float, complex
sequence types: list, tuple, range
mapping type: dict
set types: set frozenset
boolean type: bool
binary types: bytes, bytearray, memoryview
none type: NoneType
"""

"""
copy list exp: list2 = list1.copy()
making a copy of a list: list2 = list(list1)
list2 = list[:]

join two list: lits3 = list1 + list2
extend the list:

"""


"""
TUPLE
Use ()
del MyTuple()


WHATS THE DIFFERENCE BETWEEN LIST TUPLE AND RANGE

For list,its availabe

UNPACK TUPLE

using asterisk: if the number of var less than those value to be assigned the us * to some of var 


LOOP TUPLES



"""

"""
SET

add(): add elements to set
clear(): remove all elements in list
copy(): return a copy of the set
difference(): - return a set containing the difference between two or more sets
difference_update(): -= removes the items in this set that are also included another set
discard(): remove the specified item
intersection(): & return a set that is the intersection of two other sets
intersection_update(): &= removes the items in this set that are not present in other specified set(s)
isdisjoint(): returns whether two sets have a intersection or not 
issubset(): <= return whether another set contains this set or not
issuperset(): >= returns whether this set contains another set ot not
             > returns whether all items in other, specified set(s) is present in this set
pop(): removes an element from the set
remove(): removes the specified element
symmetric_difference(): ^ return a set with the symmetric differences of two sets.
symmetric difference update(): ^= inserts the symmetric differences from this set and another
union(): | return a set containing the union of sets
update(): |= update the set with the union of set and others


"""







"""
DICTIONARY
get method can print the key from dictionary

"""