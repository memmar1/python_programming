total = 0
count = 0
while True:
    inp = input("1. enter an input (type done to finish): ")
    if inp.lower() == "done":
        break
    value = float(inp)
    total = total+value
    count = count+1
average  = total/count
print ("1. average of all the inputs: ", average)

#another method
numlist = []
while True:
    num1 = input("2. enter an input (type done to finish): ")
    if num1.lower() == "done":
        break
    value=float(num1)
    numlist.append(value)
average2 = sum(numlist)/len(numlist)
print ("2. average of all the inputs: ", average2)