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
d = 0
n = []    # FINAL MATRIX
while d < nR2:
    j = 0
    k = []
    d += 1
    while j < nC2:
        b2 = float(input("Enter a number: "))
        k.append(b2)
        j += 1
    n.append(k)
print(n)

result = []
if nC1 == nR2:
    x = 0
    while x < nR1:
        ans = []
        y = 0
        while y < nC2:
            t = 0
            z = 0
            while z < nC1:
                t += m[x][z] * n[z][y]
                z += 1
            ans.append(t)
            y += 1
        x += 1
        result.append(ans)
else:
    print("Multiplication is not possible")

print(result)
