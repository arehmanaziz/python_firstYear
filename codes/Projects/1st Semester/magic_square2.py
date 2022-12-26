x = int(input("Enter the dimension of matrix: "))
a = []
for i in range(x):
    b = []
    for j in range(x):
        f = int(input("Enter a number: "))
        b.append(f)
    a.append(b)

print("The Matrix:")
print("===========")
for i in range(x):
    for j in range(x):
        print(a[i][j], end="\t")
    print()

s = []
d1 = 0
d2 = 0
for i in range(x):
    d1 += a[i][i]
    d2 += a[i][-(i+1)]
    sum_r = 0
    sum_c = 0
    for j in range(x):
        sum_r += a[i][j]
        sum_c += a[j][i]
    s.append(sum_r)
    s.append(sum_c)
    print(f"The sum of row {i+1} is: ", sum_r)
    print(f"The sum of column {i+1} is: ", sum_c)
s.append(d1)
s.append(d2)
print("The sum of MAIN DIAGONAL is: ", d1)
print("The sum of ANTI DIAGONAL is: ", d2)

f = 0
for i in range(len(s)):
    if s[i] != s[0]:
        f = 1
        break

if f == 0:
    print("The Matrix is a Magic Square.")
else:
    print("The Matrix is not a Magic Square.")
