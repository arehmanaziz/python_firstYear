"""
 Simplex Method For Maximization
 ===============================

Code by: Abdur Rehman Aziz
Class: BSCS 1st Year Sec-B
Class Roll Number: 05
Seat Number: B20102009
Date of Modification: 12 / Nov / 2021
"""

from math import trunc


def makeSimplexMatrix():
    """
    Return a List of Lists of an augmented matrix,and two lists
    which contains the labels of Rows and Columns.
    In Total it Returns 3 values i.e. Matrix, Row Labels, and Column Labels
    """

    print("""
    That's how it'll display:
    
            C1      C2      C3      C4
    R1       1       0       0      4
    R2       0       1       0      5
    R3       0       0       1      6
    
    The above example is of 3x4 matrix with 3 Row Labels and 4 Column Labels
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

    return matrix, rowLabels, columnLabels   # type: # (List of Lists, List, List) respectively


def displaySimplexMatrix(matrix, rowLabels, columnLabels):
    """
    Print an augmented matrix with Labels

    Parameters:
    ----------
        matrix : list of lists
            An Augmented Matrix
        rowLabels: list
            Contains all the Row Labels
        columnLabels: List
            Contains all the Column Labels
    """

    """
    Displays the Augmented Matrix such that,
             C1      C2      C3
    R1       1       0       0
    R2       0       1       0
    R3       0       0       1
    """

    print("=" * 40)
    noOfRows = len(matrix)
    noOfColumns = len(matrix[0])

    # Finding the maximum length of a value among all the values in Matrix
    # (including all the labels) to give spaces accordingly.

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
            if z == 0:  # b/c we want to print column variables only one time
                # before the 1st row, print all the column variables
                for k in range(len(columnLabels)):
                    if k == 0:
                        # print spaces in the place of 1st column
                        print(" " * width, end=" " * 9)
                    # printing all the column labels
                    print(columnLabels[k], end=" " * (width - len(columnLabels[k]) + 6))
                print()
                z += 1   # if we don't increase it, column variables will keep get printing after each row

            if j == 0:
                # before 1st column in each row, print row variable
                print(rowLabels[i], end=" " * (width - len(rowLabels[i]) + 6))
            # printing all values of augmented matrix
            print("%8.3f" % (matrix[i][j]), end=" " * (width - len("%8.3f" % (matrix[i][j])) + 6))
        print()
    print()


def makePivotElementOne(matrix, pivotRow, pivotColumn):
    """
    Make the selected element 1

    Parameter:
    ---------
        matrix: list of lists
            An Augmented Matrix
        pivotRow: int
            Row number of matrix
        pivotColumn: int
            Column number of matrix

    Return:
    ------
        matrix: list of lists
            An Augmented Matrix with Pivot Element = 1
    """

    pivot = matrix[pivotRow][pivotColumn]  # Pivot Element
    noOfColumns = len(matrix[0])
    for i in range(noOfColumns):
        matrix[pivotRow][i] /= pivot  # Dividing all the elements of Pivot Row by Pivot Element

    return matrix  # An Augmented Matrix with Pivot Element = 1, type: List of Lists


def makePivotColumnZero(matrix, pivotRow, pivotColumn):
    """
    Make all the values of Pivot Column = 0, except for the Pivot Element

    Parameter:
    ---------
        matrix: list of lists
            An Augmented Matrix
        pivotRow: int
            Row number of matrix
        pivotColumn: int
            Column number of matrix

    Return:
    ------
        matrix: list of lists
            An Augmented Matrix with all values of Pivot Column = 0, except for the Pivot Element
    """

    noOfRows = len(matrix)
    noOfColumns = len(matrix[0])

    for i in range(noOfRows):
        if i != pivotRow:  # b/c we don't want to make Pivot Element = 0
            multiplier = matrix[i][pivotColumn]
            for j in range(noOfColumns):  # making all the values of Pivot Column = 0
                matrix[i][j] -= (matrix[pivotRow][j] * multiplier)

    return matrix  # An Augmented Matrix, type: List of Lists


def mostNegativeValue(row):
    """
    Search the SMALLEST -VE VALUE in a list

    Parameter:
    ---------
        row: list
            contains float or int type values

    Return:
    -------
        if it founds the SMALLEST -VE VALUE:
            return: index number of that value (type: int)
        else:
            return: -1 (type: int),
    """

    smallest = row[0]
    index = 0
    loop = len(row)
    for i in range(1, loop):
        if row[i] < smallest:
            smallest = row[i]
            index = i

    # Value should be -ve
    if smallest < 0:
        return index
    else:   # means matrix is optimal
        return -1


def smallestPositiveRatio(ratios):
    """
    Search the SMALLEST +VE VALUE in a list

    Parameter:
    ---------
        ratios: list
            contains all the ratios (type: float) b/w Pivot Column and Right Hand Value

    Return:
    -------
        if it founds the SMALLEST +VE VALUE:
            return: index number of that value (type: int)
        else:
            return: -1 (type: int),
    """

    smallest = abs(ratios[0][0])
    index = 0
    ind = 0
    loop = len(ratios)
    for i in range(loop):
        if smallest > ratios[i][0] > 0:
            smallest = ratios[i][0]
            index = ratios[i][1]
            ind = i

    # Ratio should be +ve
    if ratios[ind][0] > 0:
        return index
    else:   # means matrix is optimal
        return -1


def maximization():
    """
    Calls the function makeSimplexMatrix() to make a matrix and its labels
    Then finds the maximum possible value for a given problem by SIMPLEX METHOD FOR MAXIMIZATION

    Return:
         matrix: List of Lists
            Augmented Matrix
    """

    # use these values of matrix, rowLabels, columnLabels if don't want to input values again and again
    matrix = [[-5, -10, 0, 0, 0, 0], [20, 10, 1, 0, 0, 200], [10, 20, 0, 1, 0, 120], [10, 30, 0, 0, 1, 150]]
    rowLabels = ["Profit", "Resistor", "Capacitors", "Transistors"]
    columnLabels = ["X", "Y", "S1", "S2", "S3", "RHV"]

    # Assign the returning values, form function, to correct variables
    # matrix, rowLabels, columnLabels = makeSimplexMatrix()
    noOfRows = len(matrix)
    print("AUGMENTED MATRIX")
    displaySimplexMatrix(matrix, rowLabels, columnLabels)

    while True:
        # In maximization, pivot column has smallest -ve value in the 1st row
        # If there's no -ve value, then the values are optimal
        pivotColumn = mostNegativeValue(matrix[0])
        if pivotColumn == -1:   # If values are optimal
            break

        # adding all ratios in a list
        allRatios = []
        for i in range(1, noOfRows):
            if matrix[i][pivotColumn] != 0:
                ratio = matrix[i][-1] / matrix[i][pivotColumn]
                allRatios.append([ratio, i])

        # In maximization, pivot row has smallest +ve ratio b/w the pivot column and the last column
        # If there's no +ve value, then the values are optimal
        pivotRow = smallestPositiveRatio(allRatios)
        if pivotRow == -1:   # If values are optimal
            break

        matrix = makePivotElementOne(matrix, pivotRow, pivotColumn)
        matrix = makePivotColumnZero(matrix, pivotRow, pivotColumn)

    print("OPTIMAL MATRIX OF MAXIMIZATION")
    displaySimplexMatrix(matrix, rowLabels, columnLabels)
    # returning Augmented Matrix without Labels
    return matrix


mat = maximization()
