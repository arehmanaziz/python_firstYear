def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    t_matrix = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        t_matrix.append(row)

    return t_matrix
