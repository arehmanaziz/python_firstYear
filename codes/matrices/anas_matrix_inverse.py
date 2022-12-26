nc = int(input("Enter no. of columns : "))
nr = int(input("Enter no. of rows : "))
m = []
for i in range(nr):
    k = []
    for j in range(nc):
        value = float(input(f"Enter element {i + 1}{j + 1} : "))
        k.append(value)
    m.append(k)



def display():
    print("=" * 40)
    for r in range(nr):
        for c in range(nc):
            print("%7.3f" % m[r][c], end="\t")
        print()
    print("=" * 40)


display()

pr = int(input("Enter the number of row : "))
pc = int(input("Enter the number of column : "))
pr -= 1
pc -= 1
while pc >= 0 and pr >= 0:
    pivot_element = m[pr][pc]
    for col in range(nc):  # for col in range(nr):
        m[pr][col] /= pivot_element     # m[col][pc] /= pivot_element

    display()

    for row in range(nr):  # range(nc)
        if row != pr:
            const = m[row][pc]
            for col in range(nc):
                m[row][col] = m[row][col] - const * m[pr][col]

    display()
    pr = int(input("Enter the number of row : "))
    pc = int(input("Enter the number of column : "))
    pr -= 1
    pc -= 1
