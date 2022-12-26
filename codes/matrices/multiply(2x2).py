# nC = int(input("Enter no. of Columns: "))
# nR = int(input("Enter no. of Rows: "))
nR = 2
nC = 2
j = 0
m = []    # FINAL MATRIX
while j < nR:
    i = 0
    k = []
    j += 1
    while i < nC:
        a = float(input("Enter a number: "))
        k.append(a)
        i += 1
    m.append(k)
print(m)

# nC = int(input("Enter no. of Columns: "))
# nR = int(input("Enter no. of Rows: "))
nR = 2
nC = 2
j = 0
b = []    # FINAL MATRIX
while j < nR:
    i = 0
    k = []
    j += 1
    while i < nC:
        a = float(input("Enter a number: "))
        k.append(a)
        i += 1
    b.append(k)
print(b)

result = [[0, 0], [0, 0]]
for i in range(len(m)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += m[i][k] * b[k][j]

for r in result:
    print(r)
