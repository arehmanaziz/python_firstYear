from math import trunc

# matrix = [["X", "Y", "S1", "Sassafras2", "S3", "RANDOM"], ["Profit", -5, -10, 0, 0, 0, 0], ["Resistor", 20, 10, 1,
# 0, 0, 200], ["Transistorising", 10, 20, 0, 1, 0, 155], ["Capacitors", 10, 30, 0, 0, 1, 150]]
#
# noOfRows = len(matrix)
# noOfColumns = len(matrix[1])
#
# col_width = max(len(str(label)) for label in matrix[0])
# val_width = max(len(str(trunc(value))) for row in matrix[1:] for value in row[1:]) + 4
# row_width = max(len(str(row[0])) for row in matrix[1:])
#
# if row_width > col_width and row_width > val_width:
#     width = row_width
# elif col_width > row_width and col_width > val_width:
#     width = col_width
# else:
#     width = val_width
#
# print(width)
#
# z = 0
# for i in range(noOfRows):
#     for j in range(noOfColumns):
#         if z == 0:
#             z += 1
#             for k in range(len(matrix[0])):
#                 if k == 0:
#                     print(" " * width, end=" " * 9)
#                 print(matrix[i][k], end=" "*(width - len(matrix[i][k]) + 6))
#         if i != 0:
#             if j != 0:
#                 print("%8.3f" % (matrix[i][j]), end=" "*(width - len("%8.3f" % (matrix[i][j])) + 6))
#             else:
#                 print(matrix[i][j], end=" "*(width - len(matrix[i][j]) + 6))
#     print()


mat = [[-5, -10, 0, 0, 0, 0], [20, 10, 1, 0, 0, 200], [10, 20, 0, 1, 0, 120], [10, 30, 0, 0, 1, 150]]
rowLabel = ["Profit", "Resistor", "Capacitors", "Transistors"]
columnLabel = ["X", "Y", "S1", "S2", "S3", "RHV"]


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


displaySimplexMatrix(mat, rowLabel, columnLabel)
