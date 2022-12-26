d = { "a":2, "b":3, "c":4 }
# this is called key-value pairs
print(type(d))
print(id(d))

k = d.keys()
print(k)

v = d.values()
print(v)

d['b'] = 45
print(d)

i = d.items()
print(i)

l = list(k)
print(l)