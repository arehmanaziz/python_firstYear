# print the total, average, and all the no.s > avg

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = 0
i = 0
n = len(a)

while i < n:
    b = a[i]
    t += b
    i += 1


avg = t / n

print('-' * 100)
i = 0
while i < n:
    if a[i] > avg:
        print("One of the no. which is greater than the avg is: {}".format(a[i]))
    i += 1
print('-' * 100)

print("The sum of all no.s is: {}".format(t))
print('-'*100)

print("The average of all no.s is: {}".format(avg))
print('-'*100)
