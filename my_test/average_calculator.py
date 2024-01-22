total = 0
count = 0
while True:
    inp = input("enter an input (type done to finish): ")
    if inp.lower() == "done":
        break
    value = float(inp)
    total = total+value
    count = count+1
average  = total/count
print ("average of all the inputs: ", average)