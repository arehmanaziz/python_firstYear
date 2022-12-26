def displayMatrix(m):
    nr = len(m)
    nc = len(m[0])
    print("****** Matrix ******")
    for i in range(nr):
        for j in range(nc):
            if j == nc-1:
                print("|", end="\t")
            print("%8.3f" % (m[i][j]), end="\t")
        print()


def matrix():
    nr = int(input("Enter no. of rows: "))
    nc = int(input("Enter no. of columns: "))
    j = 0
    m = []
    while j < nr:
        i = 0
        k = []
        while i < nc:
            a = float(input(f"Enter value of A{j+1}{i+1}: "))
            k.append(a)
            i += 1
        m.append(k)
        j += 1
    print()

    # ------    PRINT   -------
    displayMatrix(m)
    return m


def subtract(a, b, m):
    for i in range(len(m[a])):
        m[a][i] -= m[b][i]
    return m


def multiply(a, b, m):
    for i in range(len(m[a])):
        m[a][i] *= b
    return m


def mult_then_sub(firstRow, pivotRow, multiple, m):
    n = multiply(firstRow, multiple, m)
    o = subtract(firstRow, pivotRow, n)

    return o



def gauss_jordan(m):
    nr = len(m)
    for i in range(nr):
        pivotRow = i
        pivotColumn = i
        pivotElement = m[pivotRow][pivotColumn]

        if pivotElement == 0:
            print("Can't solve if any value of diagonal is ZERO")
            return None

        m = multiply(pivotRow, 1 / pivotElement, m)

        for j in range(0, nr):
            if j != pivotRow:
                m = mult_then_sub(j, pivotRow, 1/m[j][pivotColumn], m)
                displayMatrix(m)



    # for i in range(nr):
    #     print(f"X{i + 1}: {m[i][-1]}")
    return m


# mat = matrix()
mat = [[7, 5, 12, 13], [2, 5, 6, 7], [10, 4, 6, 3]]
displayMatrix(mat)
x = gauss_jordan(mat)
