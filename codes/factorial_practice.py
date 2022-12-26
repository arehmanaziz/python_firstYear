n = int(input("Enter number : "))
n_1 = int(n - 1) 
if n == 0 or n == 1:
    print(f"The factorial of {n} is 1")
elif n < 0 :
    print("The factorial of numbers less than 0 (negative numbers) does not exists")
else :        
    while n_1 > 1 :
        n *= n_1
        n_1 -= 1
    print(n)    