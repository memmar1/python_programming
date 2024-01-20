#opening a file

f = open("week_2\Day7_workingwithfile.py\sample.txt")  #copy the relative path

#print(f.read())
#print(f.read(3))  #getting the characters
#print(type(f.read()))

"""
first_line = f.readline()   #only gives the first line
second_line = f.readline()   #for printing the second line only if you do the function twice
print(first_line, second_line)
"""

"""
for x in f:
    print(x)
    """
f.close()  #closes the file

#first_line = f.readline()  #this will print an error since you have closed the file

#writting files
"""
f2 = open("week_2\Day7_workingwithfile.py\sample2.txt", "w")

f2.write("halo there am in sample2")
f2.write("\nam the second line")
#f2.close
f2 = open("week_2\Day7_workingwithfile.py\sample2.txt", "r")
print (f2.readline())
"""
#another way
f2 = open("week_2\Day7_workingwithfile.py\sample2.txt", "r+") #this adds on the previous text in sample2

f2.write("halo there this is zin12334445")
f2.write("\nthis is emma")
f2.close
f2_r = open("week_2\Day7_workingwithfile.py\sample2.txt", "a+")
print (f2.readline())
