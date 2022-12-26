nC = int(input("Enter no. of Columns: "))
nR = int(input("Enter no. of Rows: "))
j = 0
m = []    # FINAL MATRIX
while j < nR:
    i = 0
    k = []
    j += 1
    while i < nC:
        a = int(input("Enter a number: "))
        k.append(a)
        i += 1
    m.append(k)
print(m)
