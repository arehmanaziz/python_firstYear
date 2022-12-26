sd = []

f = open("F:\\Programing\\Python Work\\University Work\\save variables\\a.txt", "r")
a = f.readline()
k = 0
while k < 60:
    b = f.readline()
    c = b.split("\t")
    sd.append(c)
    k += 1
# print((type(c),c)
print(sd)

# part(b)1
s = 0
k = 0
while k < 60:
    amount = int(sd[k][3]) * int(sd[k][4])
    s += amount
    k += 1
print(s)

# part(b)2
# sale amount by month
v = int(input("Enter the month number: "))
s = 0
i = 0
while i < 60:
    if sd[i][1] == "6":
        amount = int(sd[i][3]) * int(sd[i][4])
    s += amount
    i += 1
print(s)


# sale amount of all months
v = 6
while v <= 8:
    s = 0
    k = 0
    while k < 60:
        if int(sd[k][1]) == v:
            amount = int(sd[k][3]) * int(sd[k][4])
        s += amount
        k += 1
    print("total sales of month", v, "is", s)
    v += 1


# nextpart
v = 6
sp = []
while v <= 8:
    s = 0
    k = 0
    while k < 60:
        if not (sd[k][5]) in sp:
            sp.append(sd[k][5])
        if int(sd[k][1]) == v:
            amount = int(sd[k][3]) * int(sd[k][4])
        s += amount
        k += 1
    print("total sales of month", v, "is", s)
    v += 1
print(sp)
