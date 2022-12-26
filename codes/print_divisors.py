# Ask a no. , and print all of its divisor

a = int(input("Enter an integer: "))
b = 1

while b <= a:
    if a % b == 0:
        print(b)
    b += 1