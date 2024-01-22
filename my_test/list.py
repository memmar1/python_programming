names = ["john","mary","jane", "kate"]
print(names)
print(names[-1])
print(names[0:3])
names[0] = "joh"
print(names)

import random
x = [2,4,7,9]
y = random.choice(x)
print(y)

#set
theset = {"banana", "apple","grape"}
theset2 = {"casava", "tra","blue"}
theset.update(theset2)   #joining sets
theset.remove("banana")   #removing an element
theset.add("tree")      #adds tree
print(theset,theset2)   #prints the sets differentlhy
print(theset)

#list
z = ["glen", 4 , [3,4], "sam", "peter"]
print (len(z))
for x in z:
    print("happy new year: ", x)
print (",,,,,,,,,,,,,,,")
print(z[3])

for i in range(len(z)):
    i = z[i]
    print("happy new year: ", i)

z[2] = 45   #lists are mutable you can change the items in it.
print(z)

abc = "there are thre words"
staff = abc.split()
print(staff)

for r in staff:
    print(r)

#splitinf
s = 'spam-spam-spam'
t = s.split("-")
print (s)
print (t)

#another example
v = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
n = v.split()
print (n)
email = n[1]
print (email)
lastpart = email.split("@")
print(lastpart)
print(lastpart[1])

aa = "banana"
ab = "banana"
print("aa == ab:",aa == ab)
print(aa is ab)

ba = [1,2,3]
bb = [1,2,3]
print("ba==bb: ",ba==bb)
print(ba is bb)

#funct
def delete_head(t):
    del t[0]

letters = ['a', 'b', 'c']
print(letters)
delete_head(letters)
print(letters)


