def inverse(n):
    rows = n
    columns = n
    j = 0
    m = []
    while j < rows:
        i = 0
        k = []
        while i < columns:
            a = float(input(f"Enter value of A{j + 1}{i + 1}: "))
            k.append(a)
            if i == columns - 1:
                for n in range(columns):
                    k.append(0)
                k[columns + j] = 1
            i += 1
        m.append(k)
        j += 1

    # m = [[1, 3, 4, 1, 0, 0], [5, 6, 7, 0, 1, 0], [8, 9, 10, 0, 0, 1]]
    # rows = len(m)
    # columns = len(m[0])

    print()
    print("The Matrix")
    print("=" * 20)
    col_width = max(len(str(value)) for row in m for value in row) + 2
    for i in range(rows):
        for j in range(rows):
            print("".join(str(m[i][j]).ljust(col_width)), end="\t")
        print()
    print()

    h, w = len(m), len(m[0])

    for y in range(0, h):
        maxrow = y
        for y2 in range(y + 1, h):
            if abs(m[y2][y]) > abs(m[maxrow][y]):
                maxrow = y2

        m[y], m[maxrow] = m[maxrow], m[y]

        for y2 in range(y + 1, h):
            c = m[y2][y] / m[y][y]
            for x in range(y, w):
                m[y2][x] -= m[y][x] * c

    for y in range(h - 1, -1, -1):
        c = m[y][y]
        for y2 in range(0, y):
            for x in range(w - 1, y - 1, -1):
                m[y2][x] -= m[y][x] * m[y2][y] / c
        m[y][y] /= c

        for x in range(h, w):
            m[y][x] /= c

    inv = []
    for i in range(h):
        r = []
        for j in range(h, w):
            r.append(m[i][j])
        inv.append(r)
    # -----------  PRINT  -------------
    print("Multiplicative Inverse Of The Matrix")
    print("=" * 40)
    col_width = max(len(str(value)) for row in inv for value in row) + 2
    for i in range(h):
        for j in range(h):
            print("".join(str(inv[i][j]).ljust(col_width)), end="\t")
        print()
    print()
    print(m)
    return inv


invs = inverse(3)
# print(invs)
