#Day 1 OPERATIONS AND VARIABLES

name = input("Enter your name: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


multiplication = num2*num1
addition = num1 + num2
subtraction = num1-num2
division = num1/num2
modulus = num1%num2
quatient = num1//num2
print("Multiplication:............. ", multiplication)
print("Addition:................... ", addition)
print("Subtruction:................ ", subtraction)
print("Division:................... ", division)
print("Modulus:.................... ", modulus) #modulus gives the remainder
print("Quatient:................... ", quatient) #quatient value ie how many time does 2 go into 7 ie 3 times
print("Are the two numbers the same: ",num1 == num2) #comparison either true or false
print("The square of the numbers are:",num1**2, "and", num2**2,"Respectivetly") #the Square or exponet
#print (num1 == 20 and num2 ==80) # returns true if both conditions are correct

