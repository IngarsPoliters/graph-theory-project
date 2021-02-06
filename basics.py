#Ingars Politers
#Python basics
#2021-02-05

print("Hello, world!")

a = 1
b = 1.0
s = "'Hello', world from a string!"
t = '"Hello", from a different string'

print(a, b, s, t)

print(type(a))

print(type(b))

print(s[1])

print(s[2:10])

print(s[5:10:2])

x = [1, 2, 3, "Hello", 1.0]
print(x)
print(x[0])
print(x[2])
print(x[-1])

print("_______________________")

for i in x[::2]:
    print(i)
    print(i + i)

for i in range(100):
    print(i)
    
d = {"no_wheels": 4, "make": "Skoda"}

print(d["make"])

d["model"] = "Superb"

print(d["model"])

r = [1,2,3,4]

print(r)

s = [i*i for i in r]

print(s)