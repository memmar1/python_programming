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
