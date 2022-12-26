"""Problem Statement: Little Robert likes mathematics. Today his teacher has given him two integers and asked to find
 out how many integers can divide both the numbers. Would you like to help him in completing his school assignment?

Input Formatting: There are two integers, a and b as input to the program.

Output Formatting: Print the number of common factors of a and b.
 Both the input value should be in a range of 1 to 10^12."""

num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
maximum = max(num1, num2)

j = 1
for i in range(2, maximum):
    if (num1 % i == 0) and (num2 % i == 0):
        j += 1

print(j)