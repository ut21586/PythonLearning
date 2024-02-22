a = """
    it ssosososososo great,
    to see you and wish you,
    all the best.
    """

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