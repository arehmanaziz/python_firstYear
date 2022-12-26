# factorial = 1
#
# if num < 0:
#     print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#     for i in range(1,num + 1):
#         factorial *= i
#     print("The factorial of",num,"is",factorial)

#                                     --------OR---------

num = int(input("Enter an integer: "))
b = int(num - 1)
if num < 0:
    print("Sorry, factorial does not exist for -ve numbers")
elif num == 0 or num == 1:
    if num == 0:
        print("The factorial of 0 is 1")
    if num == 1:
        print("The factorial of 1 is 1")
else:
    while b > 0:
        c = num
        num *= b
        b -= 1
    print("The factorial is ", num)
