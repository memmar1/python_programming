n=1
while n<6:
    print(n)
    n = n +1
else:
    print ("n is nolonger less than 6")

n=1
while n<6:
    print(n)
    if n==3:
        break
    n = n+1
print ("finish")

n=1
while n<6:
    n = n+1
    if n==3:
        continue
    print(n)
print ("finish")
