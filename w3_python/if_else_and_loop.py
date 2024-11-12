
#python 's if...else
"""
Equals: a==b
not Equals: a != b
less than: a < b
less than or equal to: a <= b
greater than: a > b
greater than or equal to: a >= b
"""
a = 100
b = 30
print("a is greater than b") if a > b else print("nope haven't got the answer") if not a == b else print ("nope wrong answer")

#python has 2 primitive loop commands:
#while loops
#for loops
#the break statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
    if i == 4:
        continue
    print(i)
else:
    print("i is less than6")



    