
string1= "hepllo There p, Welcome"
print("my string has a size of :", len(string1))
print(" last elemt", string1[-1])
print(" the first 5 elements", string1[0:5])

string2 = "this is string 2"
string3 = string1 +" "+ string2
print("concatnated strings:",string3)

 #formating strings
combined_string = f"{string1} {string2}"
print("concatnated strings:",combined_string)

#string methods
#capitalize elements
print("capitaalzed string:", string1.capitalize())
#capitalise all 
print("capitaalzed string:", string1.upper())
print("capitaalzed string:", string1.lower())#changes all to lower case

#how many times an elent appears
print("the count of 4 is:", string1.count("e")) #note that its case sensitive

print("the count of p is:", string1.lower().count("p")) #can 1st put all in lower

#finding index of a string
print("index of p in string:", string1.find("p"))
print("index of e in string:", string1.find("e"))
#what is there are more than 2 ps???

for index, char in enumerate(string1.lower()):
    if char == "p":
        print(f"{index}: {char}")

        """
index=0
string4 = "emmanuel"
for char in string4:
    print(f"{index}":{char}")
    index=index+1
"""
#spliting a string
print("split string:", string1.split(" "))

print("the index of p:",string1.find("p"))


