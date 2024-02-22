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
n = "helloword"
print(a.upper())

