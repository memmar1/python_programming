#FUNCTIONS
"""
#case 1
def function ():
    print ("halla emmar")

function()


#case2 additing 2 input variables
def summation (a,b):
    sum = a+b
    print (a)
    print ("the result of you function is: ",sum)   #result print (sum)
summation(2,3)

#compund intrest fomulla
def compound_intrest_calculator(principle,rate,time):
    amount = principle*(1 + rate)**time
    print("Compound intrest is: ", amount)

compound_intrest_calculator(10000,2,12)


#volume
def volume (length, width, height):
    v = length*width*height
    print ("the Volume is:", v)

volume(3.2,4,2) 
"""

#scope of variables
#local variable
def summation (a,b):
    sum = a+b
    print (a)   #local variable
    print ("the result of you function is: ",sum)   #result print (sum)

value1 = 3     #globsl variable
value2 = 5      #global variable
summation(value1,value2)
"""print(b)  #its not within the function so it will bring an error"""

big = max("10","23")
print(int(big))  #biggest int is 23

big = max("hallo world")  #max takes the largest ie w here is the biggest in the alphbet
print(big)

big = min("hallo world")  #min takes the smallest  blank here is the smallest in the alphbet ie a
print(big)

x = ("231345 43434")
print(len(x))       #lenth of a variable including the space

print(type(x))
print(type(big))

import math
print (math)
a = math.pi *3
c = math.log10(9) * 3
b = math.sqrt(4)
print ("c =",c)
print("a = ", a)
print("square root of b is", b)

import datetime

#random numbers
import random
z= ["q","2","t","p","78"]
for i in range(4):     #prints in range of 4 any 4 random numbers ie it etrates 4 times 
    i = random.choice(z)
    print (i)

numbers = [4,2,5,4,5,6,7]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
    print(numbers[i])

print(z[1:3])  #splicing a list
print(z[:3])  #splicing a list
print(z[3:])  #splicing a list
print(type(z)) 
numbers.append("9") 
print(numbers)
print(3 in numbers)
print(12 in numbers)
z.sort()
print(z)

