def matrix(numberOfRows, numberOfColumns, matrixName):
    m = []
    for i in range(numberOfRows):
        k = []
        for j in range(numberOfColumns):
            b = float(input(f"Enter a number for matrix {matrixName}: "))
            k.append(b)
        m.append(k)
    return m

def matrix_x(a, b):
    result = []
    nR1 = len(a)
    nC1 = len(a[0])
    nR2 = len(a)
    nC2 = len(b[0])
    if nC1 == nR2:
        for x in range(nR1):
            ans = []
            for y in range(nC2):
                t = 0
                for z in range(nC1):
                    t += a[x][z] * b[z][y]
                ans.append(t)
            result.append(ans)
    else:
        print("Multiplication is not possible.")
    return result

# c = matrix(2, 2, "c")
# d = matrix(2, 2, "d")
# e = matrix_x(c, d)
# print(c, d, e, sep="\n")