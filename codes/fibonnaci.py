# fibonacci method
# index     1 2 3 4 5 6 7 8  ........ 
#           | | | | | | | |
# Example   0 1 1 2 3 5 8 13 ........ nth
# sum of last 2 numbers.

a = int(input("Enter number : "))
def fibonacci (x) :
    if x == 0 or x == 1 :
       return 1
    else:
        return fibonacci(x - 1) * x
    
print(fibonacci(a))    
