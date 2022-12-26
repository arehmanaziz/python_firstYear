def matrix(nr):
    # j = 0
    # m = []
    # while j < nr:
    #     i = 0
    #     k = []
    #     while i < nr + 1:
    #         if i == nr:
    #             a = float(input(f"Enter Augmented Matrix Coefficient {j+1}: "))
    #             k.append(a)
    #         else:
    #             a = float(input(f"Enter value of A{j+1}{i+1}: "))
    #             k.append(a)
    #         i += 1
    #     m.append(k)
    #     j += 1
    # print()
    # m = [[4,5,3,10], [3,6,7,8], [2,3,0,8]]
    m = [[0, 0, 1, 10], [0, 1, 0, 8], [1, 0, 0, 8]]

    # ------    PRINT   -------
    print("The Augmented Matrix")
    print("=" * 20)
    print()
    col_width = max(len(str(value)) for row in m for value in row) + 2
    for i in range(nr):
        for j in range(nr + 1):
            if j == nr - 1:
                print("".join(str(m[i][j]).ljust(col_width)), sep="\t", end="|")
                print(end="\t")
            else:
                print("".join(str(m[i][j]).ljust(col_width)), end="\t")
        print()
    print()
    return m


def sub_rows(a, b, m):
    for i in range(len(m[0])):
        m[a][i] -= m[b][i]
    return m


def interchange(a, b, m):
    m[a], m[b] = m[b], m[a]
    return m


def multiply(c, a, m):
    for i in range(len(m[a])):
        m[a][i] *= c
    return m


def multiply_sub(c, a, b, m):
    m = multiply(c, a, m)
    m = sub_rows(b, a, m)
    return m


def gauss_jordan(m, eps=1.0 / (10 ** 10)):
    h, w = len(m), len(m[0])

    for y in range(0, h):
        maxrow = y
        for y2 in range(y + 1, h):
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2

        if m[y][y] == 0:
            print("Not Possible By Gauss Jordan Method")
            break
        interchange(y, maxrow, m)
        if abs(m[y][y]) <= eps:
            print("Can't solve the problem by Gauss Jordan Method")
            return None

        for y2 in range(y + 1, h):
            c = m[y2][y] / m[y][y]
            multiply_sub(c, y, y2, m)

    for y in range(h - 1, -1, -1):
        c = m[y][y]
        for y2 in range(0, y):
            for x in range(w - 1, y - 1, -1):
                m[y2][x] -= m[y][x] * m[y2][y] / c
        m[y][y] /= c

        for x in range(h, w):
            m[y][x] /= c

    # -----------  PRINT  -------------
    print("The Solution Matrix")
    print("=" * 20)
    col_width = max(len(str(value)) for row in m for value in row) + 2
    for i in range(h):
        for j in range(h + 1):
            if j == h - 1:
                print("".join(str(m[i][j]).ljust(col_width)), sep="\t", end="|")
                print(end="\t")
            else:
                print("".join(str(m[i][j]).ljust(col_width)), end="\t")
        print()
    print()

    for i in range(h):
        print(f"X{i + 1}: {m[i][-1]}")
    return m


a = input()
A = matrix(3)
B = gauss_jordan(A)
