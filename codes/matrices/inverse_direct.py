def interchange(a, b, m):
    m[a], m[b] = m[b], m[a]
    return m


def subtracting(a, b, m):
    for i in range(len(m[a])):
        m[a][i] -= m[b][i]
    return m


def multiply(a, b, m):
    for i in range(len(m[a])):
        m[a][i] *= b
    return m


def multiply_sub(c, a, b, m):
    m = multiply(a, c, m)
    m = subtracting(b, a, m)
    return m


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
    # m = [[2, 3, 4, 1, 0, 0], [3, 6, 7, 0, 1, 0], [8, 6, 4, 0, 0, 1]]
    print("The Matrix")
    print("=" * 20)
    col_width = max(len(str(value)) for row in m for value in row) + 2
    for i in range(rows):
        for j in range(rows):
            print("".join(str(m[i][j]).ljust(col_width)), end="\t")
        print()
    print()

    n = len(m)
    for i in range(n):
        pivot = m[0][i]
        if pivot == 0:
            print("Can't solve if any value of PIVOT is ZERO")
            return None
        m = multiply(0, 1 / pivot, m)

        for j in range(1, n):
            m1 = list(m[0])
            next_value = m[j][i]
            if next_value != 0:
                m = multiply_sub(next_value, 0, j, m)
            m[0] = m1

        if 0 < i < n:
            m = interchange(0, i, m)

        if i < n - 1:
            m = interchange(0, i + 1, m)

    inv = []
    for i in range(n):
        r = []
        for j in range(n, n * 2):
            r.append(m[i][j])
        inv.append(r)

    # -----------  PRINT  -------------
    print()
    print("Multiplicative Inverse Of The Matrix")
    print("=" * 40)
    col_width = max(len(str(value)) for row in inv for value in row) + 2
    for i in range(n):
        for j in range(n):
            print("".join(str(inv[i][j]).ljust(col_width)), end="\t")
        print()
    print()

    return inv


invs = inverse(3)
print(invs)
