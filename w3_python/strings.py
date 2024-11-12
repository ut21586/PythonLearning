a = """
    it ssosososososo great,
    to see you and wish you,
    all the best.
    """

a_rep = "\n\tthis is line 1\n\tthis is line 2\n\tthis is line3"

response = "Success"

expected = "SUCCESS"

print(a)

#string also can be treated as array
b = "helloworld"
print(b[1])

#can loop over in a string such that loop each element in an array randomly


for x in "banana": 
    print(x)
    print(len(a))


#check whether a string appear in another string
txt = "the most important thing in life"

if "free" in txt: 
                  print("yes got it")

#slicing strings
# can return a rsnge of character by using the slice syntax
#exp:
b = "Hello, world"
print(b[2:5]) #means print out from 2nd element of array to 5th element
print(b[:5]) #deefault from to start print each element until 5th element and stop compiling
print(b[2:]) #from 2nd element to teh end
print(b[-5:-2]) #count and print with opposite direction such that from right to left


#modify string
n = " Hello, World "
#re-print as capital
print(n.upper())
print(n.lower())
#remove useless white space
print(n.strip())
print(n.replace("H", "J")) #replace H with J
print(n.split(",")) #split each element accoding what you mention in here mention as ","
                    #then program know should be mention according "," in original string

#string concatenation字符串链接
c = "hi"
d = "bro"
print(c + " " + d)

#string format


#use format method toinsert number into string
age = 36 
txt = "my name is python, iam {}"
print(txt.format(age))

#for insert multi-elements:
quality = 3
itemno = 567
price = 49.95
myorder = "i want to pay{2}dollor for{0}piece each of them{1}"
print(myorder.format(quality, itemno, price))

#escape character: used to insert a character
# \you want to insert\

# """escape character:
# single quote: \'
# backslash:\\
# newline: \n
# carriage return: \r
# tab: \t
# backspace: \b
# octal value: \ooo
# hex value: \xhh 
# """

txt = "hi welcome to the world"
txt = "hi welcome to the \"python\"world"
print(txt)
txt = "hi welcome to the \ooo python \ooo world"
print(txt)

#string method :
#all string method return newvalue instead of change original value
#python is such built-in method s that you can use on strings
"""capitalize():convert the first letter to upper-case
casefold(): converts string into lowercase
center(): returns a centered string
count(): returns the number of times a specified value occur in a string
encode(): return an encoded version of the string
endswith(): returns true if the string ends with specified value
expandtabs(): set the tab size of the string
find(): searches the string for a specified value and return the position of where is was found
format(): formats specified value in a string
format_map():formats specified value in a string
index(): searchs the string for a specified value and return the position of where it was found
isalnum(): return true if all character in the stringare alphanumeric 如果字符串中的所有字符都是字母数字，则返回True
isalpha(): return true if all character in the string are alphabet字母表
isascii(): return true if all character in the string are ascii characters 
isdecimal():return true if all character in a string are decimal
isdigit():return true if all character in string are digits
isidentifier():return true if the string is an identifier
islower():return true if all character in string are lower case
isnumeric(): return true if all character in string are numeric都是数字
isprintable(): return true if all string is printable
isspace(): return true if all character in string are whitespaces
istitle(): return true if the string follows the rules of title
isupper(): check if all character in string are upper-case return true
join(): join the elements of an iterable to end of string 
ijust(): return a left justified version of the string
lower(): converts a string in lower case
istrip(): returns a left trim version of the string 返回字符串的左修剪版本
marktrans(): returns aa translation table to be used in translations
partition(): returns a tuple where the string is parted into three parts
replace():return a string where a specified value is been replaced
rfind(): search the string for a specofoed value and return the last position of where it was found
rindex(): search the for a specifed value whcih is index and return last position
rjust(): return a right justified version of string
rpartition(): return a tuple元组 where the string a parted into 3 parts
rsplit(): split the string at the specified separator and return a list
split(): splitthe string at the specified separator and return a list
splitlines(): splits the string at line breaks and return a list
startwith(): return true if teh syring starts with specified value
strip(): returns a trimmed version of the string返回字符串的修剪版本
swapcase():swap cases
title():converts the first character of each world to uppercase
translate(): return a translated string
upper(): converts a string into upper-case
zfill(): fills the string with specofoed number of 0 values at the beginning """
