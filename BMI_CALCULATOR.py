
def bni_calculator(name1, weight,height):
    bni = weight / (height**2)
    print(f"bmi: ",bni)
 
    if bni < 18:
        print( name1, "of", age, "year")
        return "You are under weigth."
    elif bni < 25:
        print( name1, "of", age, "year")
        return "your bni is normal"
    elif bni < 30:
        print( name1, "of", age, "year")
        return "You are over weight."
    else:
        print( name1, "of", age, "year")
        return "You are orbess."

name1 = input("Enter you name: " )
age = int(input("Enter your age: "))
weight = int(input("enter you weight in kgs: "))
height = int(input("enter you height in m: "))

result = bni_calculator(name1, weight,height)
print(result)