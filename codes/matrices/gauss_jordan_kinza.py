def matrix():
    print("Input a augmented matrix")
    R = float(input("enter number of rows "))
    C = float(input("enter number of columns "))
    c = []
    j = 0
    while j < R:
            i = 0
            b = []
            while i < C:
                z = float(input("enter a number:"))
                b.append(z)
                i += 1
            j += 1
            c.append(b)
    print(c)

def subrow(mat, constant, row2):
    a = len(mat[row2])
    for i in range(a):
        a = constant * mat[0][i]
        mat[row2][i] = mat[row2][i] - a

def constantdivide(mat, constant):
    a = len(mat[-1])
    for i in range (a):
        if constant != 0: mat[0][i] = mat[0][i] / constant
        else:print("can't divided a number by zero")

def interchangerows(mat, row1, row2):
        a = mat[row1]
        mat[row1] = mat[row2]
        mat[row2] = a

def gauss(c):
    R = len(c)
    j = 0
    k = 1
    while j < R:
        pivot = c[0][j]
        constantdivide(c, pivot)
        i = 1
        while i < R:
            y = c[i][j]
            subrow(c, y, i)
            i += 1
        interchangerows(c, 0, k)
        if k < R-1: k += 1
        j += 1
    print(c)
    for i in range(R):
        ans = c[i][-1]
        print("The solution of the equation is", ans)

d = [[7, 5, 12, 13], [2, 5, 6, 7], [10, 4, 6, 3]]
gauss(d)