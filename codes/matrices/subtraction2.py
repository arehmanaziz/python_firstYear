print("For 1st Matrix")
nC1 = int(input("Enter no. of Columns: "))
nR1 = int(input("Enter no. of Rows: "))
a = 0
m = []    # FINAL MATRIX
while a < nR1:
    i = 0
    k = []
    a += 1
    while i < nC1:
        b1 = float(input("Enter a number: "))
        k.append(b1)
        i += 1
    m.append(k)
print(m)

print("For 2nd Matrix")
nC2 = int(input("Enter no. of Columns: "))
nR2 = int(input("Enter no. of Rows: "))
a = 0
n = []    # FINAL MATRIX
while a < nR2:
    i = 0
    k = []
    a += 1
    while i < nC2:
        b2 = float(input("Enter a number: "))
        k.append(b2)
        i += 1
    n.append(k)
print(n)

result = []
if nR1 == nR2 and nC1 == nC2:
    for i in range(nR1):
        r = []
        for j in range(nC1):
            r.append(m[i][j] - n[i][j])
        result.append(r)
    print(result)
else:
    print("Addition is not possible")
