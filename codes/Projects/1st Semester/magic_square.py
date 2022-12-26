x = int(input("Enter the dimension of square you want: "))
a = []
for i in range(x):
    b = []
    for j in range(x):
        f = int(input("Enter a number: "))
        b.append(f)
    a.append(b)
print(a)

for i in range(x):
    for j in range(x):
        print(a[i][j], end=" ")
print()

sum_d1 = 0
sum_d2 = 0
for i in range(x):
    for j in range(x):
        if i == j:      # for diagonal.
            sum_d1 += a[i][j]
        if i + j == x - 1:  # for minor diagonal
            sum_d2 += a[i][j]

if sum_d1 != sum_d2:
    f = 1
else:
    for i in range(x):
        sum_r = 0
        sum_c = 0
        for j in range(x):
            sum_r += a[i][j]
            sum_c += a[j][i]
    if sum_r != sum_d1:
        f = 1
    elif sum_c != sum_d1:
        f = 1
    elif sum_c != sum_r:
        f = 1
    else:
        f = 0
if f == 0:
    print("Matrix is a Magic Square.")
else:
    print("Matrix is not a Magic Square.")
