
for i in range (1,6):
    for j in range(1, i+1):
        print(j, end="")
    print()

x = ["1","2","3","4","5"]
for i in x:
    print(i)

friends = ["jana", "kate", "mass","james"]
for friend in friends:
    print ("mary xmas", friend)

#finding the largest number
largest = -1
selection = [3,30,45,76,467,43,56,78,6,980]
print ("before: ", largest)
for num in selection:
    if num > largest:
        largest = num
    print(largest, num)
print("after: ",largest)

#countig the members in the list
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
    print(itervar)
print('Count: ', count)

#the total of all the numbers in the list
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
    print(itervar)
print('Count: ', total)

#finding the smallest number
smallest = None   #or you can put a very big number here
selection = [3,30,45,76,467,43,56,78,6,980]
print ("before: ", smallest)
for num in selection:
    if smallest is None or num < smallest:
        smallest = num
    print(smallest, num)
print("after: ",smallest)

smallest = None   #or you can put a very big number here
selection = [3,30,45,76,467,43,56,78,6,980]
print ("before: ", smallest)
for num in selection:
    if smallest is None:
        smallest = num
    elif num < selection:
         smallest = num
    print(smallest, num)
print("after: ",smallest)