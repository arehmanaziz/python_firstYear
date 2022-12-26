# print only even no.s present inside the list

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        print(a[i])
    i += 1