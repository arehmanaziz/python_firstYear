def dispmatrix(Matrix):
    noOfRows = len(Matrix)
    noOfColumns = len(Matrix[0])
    for r in range(noOfRows):
        for c in range(noOfColumns):
            if r == 0:
                print((Matrix[r][c]), end="  \t      ")
            elif c == 0 and r > 0:
                print((Matrix[r][c]), end="\t   ")
            else:
                print("%10.3f" % (Matrix[r][c]), end="\t")
        print()

    print("______________________________________________________________________________________")


# def Inputmatrix():
#     nC = int(input("Enter No. Of Columns: "))
#     nR = int(input("Enter No. Of Rows: "))
#     M=[]
#     for r in range (nR):
#         R=[]
#         for c in range (nC):
#             element=float(input("M["+str(r)+","+str(c)+"]= "))
#             R.append(element)
#         M.append(R)
#     return M
def arrangematrix(M):
    A = []
    for i in range(len(M[0])):
        if (i == 0):
            a = "          "
            A.append(a)
        Head = input("Enter Heads by order: ").upper()
        A.append(Head)
    C = []
    C.append(A)
    for i in range(1, len(M) + 1):
        B = []
        name = input("Enter Name of Acc to Order: ").upper()
        if (name == "PROFIT"):
            name = "PROFIT  "
        B.append(name)
        C.append(B)

    k = 1
    for i in range(len(M)):

        for j in range(len(M[0])):
            C[k].append(M[i][j])
        k = k + 1

    dispmatrix(C)


def smalminusval():
    smallest = M[0][0]
    index = 0
    bol = 'n'
    for i in range(len(M[0])):
        if (M[0][i] <= smallest and M[0][i] < 0):
            smallest = M[0][i]
            index = i
            bol = 'y'
    if (bol == 'y'):
        return index
    else:
        return -1


def MakePivotOne(Matrix, PivotRow, PivotColumn):
    NoOfcolumns = len(Matrix[0])
    PivElement = Matrix[PivotRow][PivotColumn]
    for c in range(NoOfcolumns):
        Matrix[PivotRow][c] = (Matrix[PivotRow][c]) / PivElement
    return Matrix


def MakePivotZero(Matrix, PivotRow, PivotColumn):
    RowNumber = len(Matrix)
    NoOfColumn = len(Matrix[0])
    for r in range(RowNumber):
        if r != PivotRow:
            cons = Matrix[r][PivotColumn]
            for c in range(NoOfColumn):
                Matrix[r][c] = (Matrix[r][c]) - (cons * (Matrix[PivotRow][c]))
    return Matrix


# _________________________________MAIN________________________________________________
M = [[-5.000, -10.000, 0.000, 0.000, 0.000, 0.000], [20.000, 10.000, 1.000, 0.000, 0.000, 200.000],
     [10.000, 30.000, 0.000, 1.000, 0.000, 150.000], [10.000, 20.000, 0.000, 0.000, 1.000, 120.000]]


# M=Inputmatrix()

def leastratio(PivotColumn):
    leastRatio = M[1][-1] / M[1][PivotColumn]
    index = 0
    for i in range(1, len(M)):
        if (leastRatio >= M[i][-1] / M[i][PivotColumn]):
            leastRatio = M[i][-1] / M[i][PivotColumn]
            index = i
    return index


dispmatrix(M)
PivotColumn = smalminusval()
PivotRow = leastratio(PivotColumn)
# PivotColumn=int(input("Enter Pivot Column : ")) -1
while PivotRow >= 0 and PivotColumn >= 0:
    MakePivotOne(M, PivotRow, PivotColumn)
    RowNumber = len(M)
    for r in range(RowNumber):
        MakePivotZero(M, PivotRow, PivotColumn)

    PivotColumn = smalminusval()
    PivotRow = leastratio(PivotColumn)

arrangematrix(M)
