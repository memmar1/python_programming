
kg = float(input("Weigth in kg: "))
unit = input ("enter (g) for grams or (l) for pound: ")
g = (kg * 1000)
bs = (kg * 2.20462)

if unit == "g".upper():
    print("Wiegth in gram is ",g,"g" )
elif unit == "l".upper():
    print("weight in pounds is ", bs, "l")
else:
    print ("wrong input")