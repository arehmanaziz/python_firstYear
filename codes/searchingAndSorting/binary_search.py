values = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
start = 0
end = len(values) - 1
a = int(input("Please enter the value you want to search: "))
b = 0
for i in range(len(values)):
    mid = (start + end)//2
    middle = values[mid]
    if middle == a:
        b = 1
        break

    elif middle < a:
        start = mid

    elif middle > a:
        end = mid

if b == 1:
    print(f"{a} found at position {mid + 1}")
else:
    print(f"{a} is not present in the list")

