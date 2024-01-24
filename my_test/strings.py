line = "please this is a game"
ni = line.capitalize()
print(ni)
xi = line.upper()
print(xi)
ri = line.startswith("p")
print(ri)
ri = line.startswith("the")
print(ri)

data = "  from steven.mark@uct.ac.za sat jan 5 09:14:16"
art = data.find("@")
print(art)
opp = data.find(" ",art)
print(opp)
host = data[art+1:opp]
print(host)
n = data.strip()
print(n)
print(data)

#fomatting string
num = 45
f = f"{num}"
print(type(f))
print(type(num))

years = 3
count = .1
species = 'camels'
st = f"In {years} years I have spotted {count} {species}."
print(st)