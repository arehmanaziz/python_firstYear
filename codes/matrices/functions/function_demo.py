from matrices.functions import matrix_func

a = matrix_func.matrix(3, 2, "a")
b = matrix_func.matrix(2, 3, "b")
c = matrix_func.matrix_x(a,b)
print(a, b, c, sep="\n")