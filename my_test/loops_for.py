fruits = ["apples", "bananas", "oranges"]
for w in fruits:
    print(w)


fruits = ["apples", "bananas", "oranges"]
for w in "oranges":
    print(w)


fruits = ["apples", "bananas", "oranges"]
for w in fruits:
    print(w)
    if w == "bananas":
        break
print("  ")

fruits = ["apples", "bananas", "oranges"]
for w in fruits:
    if w == "bananas":
        continue
    print(w)
print ("Done")

fruits = ["apples", "bananas", "oranges"]
adj = ["red", " black", "blue"]
for x in adj:
    for y in fruits:
        print(x,y)

num1 = [1]
num2 = [1,2,3,4,5]
for x in num1:
    for y in num2:
        print(x,y)