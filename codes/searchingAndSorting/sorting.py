a = [61, 32, 54, 22, 91, 100, 36, 48, 50, 1, 44]
n = len(a)
print(a)
j = 0
while j < n:
    s = a[j]
    p = j
    i = j + 1
    while i < n:
        if a[i] < s:
            s = a[i]
            p = i
        i += 1
    t = a[j]
    a[j] = a[p]
    a[p] = t
    j += 1
print(a)
