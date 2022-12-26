from pandas import DataFrame as df
from math import trunc


def makeMatrix():
    noOfRows = int(input("Enter no. of rows: "))
    noOfColumns = int(input("Enter no. of columns: "))
    matrix = []
    for i in range(noOfRows):
        k = []
        for j in range(noOfColumns):
            a = float(input(f"Enter value of Matrix {i + 1}{j + 1}: "))
            k.append(a)
        matrix.append(k)

    return matrix


def makeSimplexMatrix():
    noOfRows = int(input("Enter no. of rows: "))
    noOfColumns = int(input("Enter no. of columns: "))

    columnLabels = []
    rowLabels = []

    print("Enter all the Row Labels 1 by 1 in sequence")
    for i in range(noOfRows + 1):
        label = input(f"Enter Row Label {i + 1}: ")
        rowLabels.append(label)

    print("Enter all the Column Labels 1 by 1 in sequence")
    for i in range(noOfColumns):
        label = input(f"Enter Column Label {i + 1}: ")
        columnLabels.append(label)

    matrix = []
    for i in range(noOfRows):
        k = []
        for j in range(noOfColumns):
            a = float(input(f"Enter value of Matrix {i + 1}{j + 1}: "))
            k.append(a)
        matrix.append(k)

    return matrix, rowLabels, columnLabels


def displayMatrix(matrix):
    noOfRows = len(matrix)
    noOfColumns = len(matrix[0])
    print("AUGMENTED MATRIX")
    print("=" * 20)
    for i in range(noOfRows):
        for j in range(noOfColumns):
            print("%8.3f" % (matrix[i][j]), end="\t")
        print()
    print()


def displaySimplexMatrixPanda(matrix, rowLabels, columnLabels):
    display = df(matrix, columns=columnLabels, index=rowLabels)
    print(display)


def displaySimplexMatrix(matrix, rowLabels, columnLabels):
    print("=" * 40)
    noOfRows = len(matrix)
    noOfColumns = len(matrix[0])

    row_width = max(len(str(label)) for label in rowLabels)
    col_width = max(len(str(label)) for label in columnLabels)
    val_width = max(len(str(trunc(value))) for row in matrix for value in row) + 4

    if row_width > col_width and row_width > val_width:
        width = row_width
    elif col_width > row_width and col_width > val_width:
        width = col_width
    else:
        width = val_width

    z = 0
    for i in range(noOfRows):
        for j in range(noOfColumns):
            if z == 0:
                for k in range(noOfColumns):
                    if k == 0:
                        print(" " * (width + 2), end=" " * 7)
                    if i != noOfRows - 1:
                        print(columnLabels[k], end=" " * (width - len(columnLabels[i + 1]) + 6))
                    else:
                        print(columnLabels[k])
                print()
                z += 1

            if j == 0:
                print(rowLabels[i], end=" " * (width - len(rowLabels[i]) + 6))

            if len(columnLabels[j]) == width or len(columnLabels[j]) > len("%8.3f" % (matrix[i][j])):
                if j != noOfColumns - 1:
                    print("%8.3f" % (matrix[i][j]),
                          end=" " * (len(columnLabels[j]) + width - len("%8.3f" % (matrix[i][j + 1])) + 6))
                else:
                    print("%8.3f" % (matrix[i][j]))

            else:
                if j != noOfColumns - 1:
                    print("%8.3f" % (matrix[i][j]), end=" " * (width - len("%8.3f" % (matrix[i][j + 1])) + 6))
                else:
                    print("%8.3f" % (matrix[i][j]))
    print()


def makePivotElementOne(matrix, pivotRow, pivotColumn):
    pivot = matrix[pivotRow][pivotColumn]
    noOfColumns = len(matrix[0])
    for i in range(noOfColumns):
        matrix[pivotRow][i] /= pivot

    return matrix


def makePivotColumnZero(matrix, pivotRow, pivotColumn):
    # pivot = matrix[pivotRow][pivotColumn]
    noOfRows = len(matrix)
    noOfColumns = len(matrix[0])

    for i in range(noOfRows):
        if i != pivotRow:
            multiplier = matrix[i][pivotColumn]
            for j in range(noOfColumns):
                matrix[i][j] -= (matrix[pivotRow][j] * multiplier)

            # matrix = subtractionOfRows(matrix, i, pivotRow)

    return matrix


def subtractionOfRows(matrix, row1, row2):
    noOfColumns = len(matrix[row1])
    for i in range(noOfColumns):
        matrix[row1][i] -= matrix[row2][i]

    return matrix


def smallestNegativeValue(row):
    smallest = row[0]
    index = 0
    loop = len(row)
    for i in range(1, loop):
        if row[i] < smallest:
            smallest = row[i]
            index = i

    if smallest < 0:
        return index
    else:
        return -1


def smallestPositiveRatio(ratios):
    smallest = abs(ratios[0])
    index = 0
    loop = len(ratios)
    for i in range(loop):
        if smallest > ratios[i] > 0:
            smallest = ratios[i]
            index = i

    if ratios[index] > 0:
        return index + 1
    else:
        return -1


def maximization():
    # matrix, rowLabels, columnLabels = makeSimplexMatrix()
    matrix = [[-5, -10, 0, 0, 0, 0], [20, 10, 1, 0, 0, 200], [10, 20, 0, 1, 0, 120], [10, 30, 0, 0, 1, 150]]
    rowLabels = ["Profit", "Resistor", "Resistance", "Capacitors"]
    columnLabels = ["X", "Y", "S1", "RIGHT HAND VALUE", "S3", "RHV"]

    noOfRows = len(matrix)
    print("AUGMENTED MATRIX")
    displaySimplexMatrix(matrix, rowLabels, columnLabels)

    while True:
        pivotColumn = smallestNegativeValue(matrix[0])
        if pivotColumn == -1:
            break

        allRatios = []
        for i in range(1, noOfRows):
            ratio = matrix[i][-1] / matrix[i][pivotColumn]
            allRatios.append(ratio)

        pivotRow = smallestPositiveRatio(allRatios)
        if pivotRow == -1:
            break

        matrix = makePivotElementOne(matrix, pivotRow, pivotColumn)
        matrix = makePivotColumnZero(matrix, pivotRow, pivotColumn)

    print("OPTIMAL MATRIX")
    displaySimplexMatrix(matrix, rowLabels, columnLabels)
    return matrix


mat = maximization()
