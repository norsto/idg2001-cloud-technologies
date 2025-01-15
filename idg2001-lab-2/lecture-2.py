#makes comments
#numbers
3 # int
1.5 # float

0.2 + 0.1 # 0.300000

#somtimes you're going to get calculation errors

True #have to be written with an uppercase 
False

#string is made with "" or ''
#counts like others aka. 0, 1, 2, 3, 4, so on

not True #false
not False #true

#3 = 3.0 #true
3 == 3.0 #false
#3 === 3.0 #error. === = ==

3 != 4 #true

0.1 + 0.2 == 0.3 #false?

"hello" + "world" #concatination "helloworld"

"1, 2," + 3 #shows an error

"5" == 5 #false

None #null, nothing

"this is a string"[0] #t

"this is a string"[0:5] #"this "(zero to five), but for some reason its not this i

someVar = 5
x = 3.14

print(someVar)
y = someVar + x
print(y) #8.14

x**=3 #

9**0.5 #3 (square root)

x += 1 #can't do ++ or --

myList = ["hello", 45, True] #array/list 
print(myList) # ["hello", 45, True]

myList = myList + [3] 
print(myList) # ["hello", 45, True, 3]

print(myList[1]) # 45

myList[1] = 40
print(myList) # ["hello", 40, True, 3]

len(myList) # 4 length of myList is 4

myObj = {"key1": "hello", "key2": "world" } # objects is dictionaries
print(myObj) # prints the object/dictionary

gradeSteps = {
    'A': 90,
    'B': 70
}

gradeSteps["A"] #90

print(...) #ellipsis

gradeSteps["C"] = 66 
print(gradeSteps["C"]) #66

# string = str

n = 3
a = "number of people is" + n 
print(a) # number of people is 3. putting 3 in the place of n would print an error

n = 3 
b = f"number of people is {n}" 
print(b) #number of people is 3

print(3, "hello", 0.0) # 3 hello 0.0    you can use comma instead of " " to get space in between things

count = 17
if(count == 3): # don't have to use brackets
    print('== 3')
elif(count == 4):
    print('== 4')
else:
    print("something else") # something else
# : in place of {} and elif instead of else if

#while True:
    #pass #pass it/ do nothing
    #an infinete loop, can't be empty

x = 3
while x > 0:
    x -= 1
    print(x)

#python don't have a do while loop
#don't have for loops (kinda)

mySecondList = [3, 1,4, 1, 5]
for x in mySecondList:
    print(x) #3 1 4 1 5 , but vertically

for i in range(5): #range is a built in function
    print(i) # 0 1 2 3 4 , vertically

for i in "abcd":
    print(i) #a b c d , vertically

#kind of don't have switch

def myFunction(thing): # def to make a function
    #global x #shouldn't use global unless necessary
    #print(x)
    return thing.upper()
print(myFunction("hello")) #HELLO

# printing nothing is the same as return and so none ???

x = 2 
if x >= 0:
    y = True
else:
    y = False
print(y) # True

class Car:
    def __init__(self, speed, weight): #doesn't need to have the same names
        self.speed = speed #self is a constructor
        self.weight = weight

    def __str__(self):
        return f's: {self.speed}, w: {self.weight}' #kindof like the something in javascript

peugot = Car(143, 1500)
toyota = Car(200, 2000)

print(peugot)#s: 143, w:1500 
print(toyota) #s: 200, w: 2000

print(peugot.speed) #143

x = 3.14

if type(x) is int or type(x) == float:
    print("number")
else:
    print("not a number")
# number

import math
print(math.sqrt(2)) #built in

from math import sqrt
#import math as = 

#import mathplotlib.pyplot as plt

#if it's not an built import, you have to do it via terminal (pip install, if you want to install multiple things you just use a space)
#have to update libraries everytime python updates
# python modules

#if you click option and space it creates another type of space and won't trim

import anotherfile #imports another document ?? maybe, if i tdo it'll print imported
print(anotherfile.f(3)) 

#path/URI parser
#parse = analysere

"""
def get_location(path):
    ...
    return...

get_location('path/folder/document') """

#get_new_path('path/folder1/folder2/document')

#something about windows using \ as a cansel the next character so if you need a \ you have to put \\