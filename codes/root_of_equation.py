a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")

x = float(a)
ya = x**2 - 5*x + 6
if ya == 0:
    print("One of the root is: {0}".format(a))

x = float(b)
yb = x**2 - 5*x + 6
if yb == 0:
    print("One of the root is: {0}".format(b))

ab = ya * yb

if ab > 0:
    print("There is no root present in the range")

elif ab < 0:
    yc = ""
    while yc != 0:
        c = (float(a) + float(b))/2
        x = float(c)
        yc = x**2 - 5*x + 6
        ac = ya * yc
        if ac < 0:
            b = c
        bc = yb * yc
        if bc < 0:
            a = c
        if yc == 0:
            print("One of the root is: {0}".format(c))

print("Program Ends")
