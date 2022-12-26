print("Quadratic function : (a * x^2) + b*x + c")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c

if r > 0:
    x1 = (-b + r**2)/(2*a)
    x2 = (-b - r**2)/(2*a)
    print(f"There are 2 roots: {x1} and {x2}")
elif r == 0:
    x = (-b) / 2*a
    print(f"There is one root: {x}")
else:
    print("No roots, discriminant < 0.")