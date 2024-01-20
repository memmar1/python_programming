print(1)
print(1,2)
print(1,2,3)
print(1,2,3,4)
print(1,2,3,4,5)

#another way of doing this
name = input("Enter your name:" )
print ("welcome:", name)
print("")

rate = input("enter rate:")
hours = input ("enter hours: ")
pay = (int(rate) * int(hours))
print ("your pay is: " ,pay)

width = 17
height = 12.0

a = width//2
print (a)
print (type(a))

a = width/2
print (a)
print (type(a))

a = height/3
print (a)
print (type(a))

a = 1 + 2 * 5
print (a)
print (type(a))

#Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit,
#and print out the converted temperature.

celsious = float(input("Enter the temperature in celsious: "))

Fahrenheit = float((celsious* (9/5))+ 32)

print ("Fahrenheit = ", Fahrenheit, "F")