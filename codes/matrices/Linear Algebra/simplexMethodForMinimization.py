# Simplex Method For Maximization
# ===============================

from math import trunc


def makeSimplexMatrix():
    """     Create and Return a List of Lists for the values of a matrix,
            and two single lists which contains the labels of Rows and Columns.
            In Total it Returns 3 values i.e. Matrix, Row Labels, and Column Labels     """

    print("""
    That's how it'll display:
    
            C1      C2      C3
    R1       1       0       0
    R2       0       1       0
    R3       0       0       1
    
    The above example is of 3x3 matrix with 3 Row Labels and 3 Column Labels
    """)

    noOfRows = int(input("Enter no. of rows: "))
    noOfColumns = int(input("Enter no. of columns: "))

    columnLabels = []
    rowLabels = []

    # Creating List for all the Row Labels
    print("Enter all the Row Labels 1 by 1 in sequence")
    for i in range(noOfRows):
        label = input(f"Enter Row Label {i + 1}: ")
        rowLabels.append(label)

    # Creating List for all the Column Labels
    print("Enter all the Column Labels 1 by 1 in sequence")
    for i in range(noOfColumns):
        label = input(f"Enter Column Label {i + 1}: ")
        columnLabels.append(label)

    # Creating List of Lists for the values of Augmented Matrix
    matrix = []
    for i in range(noOfRows):
        k = []
        for j in range(noOfColumns):
            a = float(input(f"Enter value of Matrix {i + 1}{j + 1}: "))
            k.append(a)
        matrix.append(k)

    return matrix, rowLabels, columnLabels


def displaySimplexMatrix(matrix, rowLabels, columnLabels):
    """
    Displays the Simplex Matrix such that,
             C1      C2      C3
    R1       1       0       0
    R2       0       1       0
    R3       0       0       1
    """

    print("=" * 40)
    noOfRows = len(matrix)
    noOfColumns = len(matrix[0])

    """
    Finding the maximum length of a value among all the values in Matrix 
    (including all the labels) to give spaces accordingly.
    """
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
                # for the 1st row print all the column variables
                for k in range(noOfColumns):
                    if k == 0:
                        # skip the 1st column
                        print(" " * (width + 2), end=" " * 7)
                    if i != noOfRows - 1:  # giving spaces according to the length of next value
                        print(columnLabels[k], end=" " * (width - len(columnLabels[i + 1]) + 6))
                    else:
                        print(columnLabels[k])
                print()
                z += 1

            if j == 0:
                print(rowLabels[i], end=" " * (width - len(rowLabels[i]) + 6))

            if len(columnLabels[j]) == width or len(columnLabels[j]) > len("%8.3f" % (matrix[i][j])):
                if j != noOfColumns - 1:
                    print("%8.3f" % (matrix[i][j]),  # giving spaces according to the length of next value
                          end=" " * (len(columnLabels[j]) + width - len("%8.3f" % (matrix[i][j + 1])) + 6))
                else:
                    print("%8.3f" % (matrix[i][j]))

            else:
                if j != noOfColumns - 1:  # giving spaces according to the length of next value
                    print("%8.3f" % (matrix[i][j]), end=" " * (width - len("%8.3f" % (matrix[i][j + 1])) + 6))
                else:
                    print("%8.3f" % (matrix[i][j]))
    print()


def makePivotOne(matrix, pivotRow, pivotColumn):
    pivot = matrix[pivotRow][pivotColumn]
    noOfColumns = len(matrix[0])
    for i in range(noOfColumns):
        matrix[pivotRow][i] /= pivot

    return matrix


def makePivotColumnZero(matrix, pivotRow, pivotColumn):
    noOfRows = len(matrix)
    noOfColumns = len(matrix[0])

    for i in range(noOfRows):
        if i != pivotRow:
            multiplier = matrix[i][pivotColumn]
            for j in range(noOfColumns):
                matrix[i][j] -= (matrix[pivotRow][j] * multiplier)

    return matrix


def mostPositiveValue(row):
    largest = row[0]
    index = 0
    loop = len(row)
    for i in range(1, loop):
        if 0 < row[i] > largest:
            largest = row[i]
            index = i

    # Value should be +ve
    if largest > 0:
        return index
    else:   # if values are optimal
        return -1


def smallestPositiveRatio(ratios):
    smallest = abs(ratios[0])
    index = 0
    loop = len(ratios)
    for i in range(loop):
        if smallest > ratios[i] > 0:
            smallest = ratios[i]
            index = i

    # Ratio should be +ve
    if ratios[index] > 0:
        return index + 1
    else:   # if values are optimal
        return -1


def minimization():
    matrix = [[5, 10, 0, 0, 0, 0], [20, 10, 1, 0, 0, 200], [10, 20, 0, 1, 0, 120], [10, 30, 0, 0, 1, 150]]
    rowLabels = ["Profit", "Resistor", "Resistance", "Capacitors"]
    columnLabels = ["X", "Y", "S1", "S2", "S3", "RHV"]
    # matrix, rowLabels, columnLabels = makeSimplexMatrix()
    noOfRows = len(matrix)
    print("AUGMENTED MATRIX")
    displaySimplexMatrix(matrix, rowLabels, columnLabels)

    while True:
        # In maximization, pivot column has smallest +ve value in the 1st row
        # If there's no +ve value, then the values are optimal
        pivotColumn = mostPositiveValue(matrix[0])
        if pivotColumn == -1:   # If values are optimal
            break

        allRatios = []
        for i in range(1, noOfRows):
            ratio = matrix[i][-1] / matrix[i][pivotColumn]
            allRatios.append(ratio)

        # In maximization, pivot row has smallest +ve ratio b/w the pivot column and the last column
        # If there's no +ve value, then the values are optimal
        pivotRow = smallestPositiveRatio(allRatios)
        if pivotRow == -1:   # If values are optimal
            break

        makePivotOne(matrix, pivotRow, pivotColumn)
        makePivotColumnZero(matrix, pivotRow, pivotColumn)

    print("OPTIMAL MATRIX")
    displaySimplexMatrix(matrix, rowLabels, columnLabels)


minimization()
