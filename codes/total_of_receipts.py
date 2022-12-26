# Print all receipt's value, and also tell its sum

t = 0
a = 0
b = []

while a >= 0:
    a = float(input("Enter receipt amount: "))
    if a >= 0:
        b.append(a)
        t += a

print('-' * 100)
print(b)

print('-' * 100)
print("The total amount is {}".format(t))

print('-' * 100)
