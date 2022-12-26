def matrix(nr):
    # j = 0
    # m = []
    # while j < nr:
    #     i = 0
    #     k = []
    #     while i < nr + 1:
    #         if i == nr:
    #             a = float(input(f"Enter Augmented Matrix Coefficient {j+1}: "))
    #             k.append(a)
    #         else:
    #             a = float(input(f"Enter value of A{j+1}{i+1}: "))
    #             k.append(a)
    #         i += 1
    #     m.append(k)
    #     j += 1
    # print()

    # ------    PRINT   -------
    m = [[5, 6, 3, 3], [2, -3, -8, 5], [3, 4, 4, 7]]
    print("The Augmented Matrix")
    print("="*20)
    print()
    col_width = max(len(str(value)) for row in m for value in row) + 2
    for i in range(nr):
        for j in range(nr + 1):
            if j == nr - 1:
                print("".join(str(m[i][j]).ljust(col_width)), sep="\t", end="|")
                print(end="\t")
            else:
                print("".join(str(m[i][j]).ljust(col_width)), end="\t")
        print()
    print()
    return m

def interchange(a, b, m) :
    m[a] , m[b] = m[b] , m[a]
    return m      

def adding(a, b, m) :
    for i in range(len(m[a])) :
        m[a][i] += m[b][i]
    return m

def subtracting(a, b, m):
    for i in range(len(m[a])):
        m[a][i] -= m[b][i]
    return m

def multiply (a, b, m) :
    for i in range (len(m[a])):
        m[a][i] *= b
    return m

def multiply_sub(c, a, b, m):
    m = multiply(a, c, m)
    m = subtracting(b, a, m)
    return m

def multiply_add(c, a, b, m):
    m = multiply(a, c, m)
    m = adding(b, a, m)
    return m

def gauss_jordan(m):
    nr = len(m)
    while True:
        l = ["a", "m", "s", "i", "e", "ms", "ma"]
        print("""
        a: To add
        s: To Subtract
        m: To multiply
        i: To swap
        ms: Multiply a row and then subtract it form another row
        ma: Multiply a row and then add it in another row
        e: To end program
        """)
        user = input("Please choose an option: ").lower()
        while user not in l:
            print("="*30)
            print("Please select a valid option")
            print("""
            a: To add
            s: To Subtract
            m: To multiply
            i: To swap
            ms: Multiply a row and then subtract it form another row
            ma: Multiply a row and then add it in another row
            e: To end program
            """)
            user = input("Please choose an option: ").lower()

        if user == "a":
            r1 = int(input("Enter the 1st row number in which you want to add : ")) - 1
            r2 = int(input("Enter the 2nd row number which you want to add : ")) - 1
            m = adding(r1, r2, m)
            print("*"*80)
            
        elif user == "s":
            r1 = int(input("Enter the 1st row number from which you want to subtract : ")) - 1
            r2 = int(input("Enter the 1st row number which you want to subtract : ")) - 1
            m = subtracting(r1, r2, m)
            print("*"*80)

        elif user == "m":
            r1 = int(input("Enter the row number you want to multiply: ")) - 1
            r2 = eval(input("Enter the constant by which you want to multiply:  "))
            m = multiply(r1, r2, m)
            print("*"*80)

        elif user == "i":
            r1 = int(input("Enter number for 1st Row : ")) - 1
            r2 = int(input("Enter number for 2nd Row: ")) - 1
            m = interchange(r1, r2, m)
            print("*"*80)

        elif user == "ms":
            r1 = int(input("Enter the row number you want to multiply: ")) - 1
            m1 = list(m[r1])
            c = eval(input("Enter the constant by which you want to multiply: "))
            r2 = eval(input("Enter the row number from which you want to subtract:  ")) - 1
            m = multiply_sub(c, r1, r2, m)
            m[r1] = m1
            print("*"*80)

        elif user == "ma":
            r1 = int(input("Enter the row number you want to multiply: ")) - 1
            m1 = list(m[r1])
            c = eval(input("Enter the constant by which you want to multiply: "))
            r2 = eval(input("Enter the row number in which you want to add:  ")) - 1
            m = multiply_add(c, r1, r2, m)
            m[r1] = m1
            print("*"*80)

        elif user == "e":
            for j in range(nr):
                if m[j][j] == 1:
                    z = 1
                else:
                    z = 0
                    break

            if z == 1:
                for i in range(nr):
                    print(f"X{i+1}: {m[i][-1]}")
            elif z == 0:
                print("Couldn't find the solution")
            break

        print("="*20)
        print()
        col_width = max(len(str(value)) for row in m for value in row) + 2
        for i in range(nr):
            for j in range(nr + 1):
                if j == nr - 1:
                    print("".join(str(m[i][j]).ljust(col_width)), sep="\t", end="|")
                    print(end="\t")
                else:
                    print("".join(str(m[i][j]).ljust(col_width)), end="\t")
            print()
        print()

    return m


mat = matrix(3)
x = gauss_jordan(mat)