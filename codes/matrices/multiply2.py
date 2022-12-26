print("For 1st Matrix")
nC1 = int(input("Enter no. of Columns: "))
nR1 = int(input("Enter no. of Rows: "))
m = []    # FINAL MATRIX
for a in range(nR1):
    k = []
    for i in range(nC1):
        b1 = float(input("Enter a number: "))
        k.append(b1)
    m.append(k)
print(m)

print("For 2nd Matrix")
nC2 = int(input("Enter no. of Columns: "))
nR2 = int(input("Enter no. of Rows: "))
n = []    # FINAL MATRIX
for a in range(nR2):
    k = []
    for i in range(nC2):
        b2 = float(input("Enter a number: "))
        k.append(b2)
    n.append(k)
print(n)

result = []
if nC1 == nR2:
    for x in range(nR1):
        ans = []
        for y in range(nC2):
            t = 0
            for z in range(nC1):
                t += m[x][z] * n[z][y]
            ans.append(t)
        result.append(ans)
    print(result)
else:
    print("Multiplication is not possible.")

