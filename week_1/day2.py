
#CONDITIONALS   IF, ELIF, ELSE, TRY AND EXCEPT
"""
a = input("Enter A: ")
b = input("EnteR B: ")

if (a >b):
    print ("A is greater than B")
elif (a < b):
    print ("A is less than B")
else: 
    print ("Please try again.")
print ("  ")


#sample2
print ("DO YOU WANT TO PROCEED?")
print ("PRESS 1 FOR YES")
print ("PRESS 2 FOR NO")
print("   ")

yes = 1
no = 2
responce  = int(input ("Enter Answer: "))

if (responce == yes ):
    print ("let us continue")
elif (responce == no):
        print ("thank you for coming")
else:
    print ("wrong input")


#sample 3
x=15
print(x)
x=x+1
print(x)

if x<10:
     print("smaller")
else:
     print("bigger")

#sample 4
y = 5
if y> 2:
     print("biger than 2")
     print("still bigger")
print ("done with 2")

for i in range (5):
     print(i)
     if i>2:
          print ("bigger than 2")
     print("done with i", i)
print ("all done")
     
#sample 5
entry = int(input("Enter entry:"))
for entry in range (6):
     print("your entry is:", entry)
     if entry>3:
          print ("entry is bigger than 3")
     print("done with entry:", entry)
print ("all done")
    
#sample 6
x=43
if x>1:
     print("bigger than 1")
     if x<100:
          print ("less than 100")
print("all done")

#sample 7
y=13
if y%2==0:
         print("its an even number")
else:
         print("its an odd number")
if y>15:
    print("bigger than 15")
    
else:

    print ("less than 15")
print("all done")

#sample  8
z = 9
if z<3:
    print ("small")
elif z<10:
      print("mediam")
else:
      print ("big")
"""
"""
#sample 9 try and except
num = input("enter number:")
try:
      xy = int(num)
except:
      xy = -1
if xy>0:
      print("nice work")
else:
      print ("not a number")

"""
#sample 9 try and except when a use inputs non digit

x = input("Enter x=")
y = input("Enter y=")

try:
    xx = float(x)  
    yy = float(y)
    if xx==yy:
        print("x is equal to y")
    elif xx<yy:
        print("x is less than y")
    else:
        print("x is great than y")
except:

    xx = -1
    yy= -1
    print("try again, please input digits")

    