a = [12, 34, 56, 50, 78, 90, 56]
n = len(a)
v = int(input("Enter the value you want to search: "))
f = "n"
for i in range(n):
    if a[i] == v:
        f = "y"
        break
if f == "y":
    print(f"The number is found at position: {i+1}.")
else:
    print("Number not found.")