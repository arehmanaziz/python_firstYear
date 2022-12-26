def reverse(text):
    txt = text[:: -1]
    return txt


def get_key(val):
    for key, value in code.items():
        if val == value:
            return key


def addition():
    num1 = reverse(input("Input 1st Number: "))
    num2 = reverse(input("Input 2nd Number: "))
    sums = ""
    carry = 0

    lengthNum1 = len(num1)
    lengthNum2 = len(num2)

    if lengthNum1 <= lengthNum2:
        num1, num2 = num2, num1
        lengthNum1, lengthNum2 = lengthNum2, lengthNum1

    for i in range(lengthNum1):
        if i < lengthNum2:
            add = str(int(num1[i]) + int(num2[i]) + carry)
            if len(add) == 2:
                sums += add[1]
                carry = int(add[0])
            else:
                sums += add
                carry = 0
        else:
            sums += num1[i]

    ans = reverse(sums)
    return ans


def encryption():
    password = "password is ABCYZX".upper()
    digits = 2
    n = 2773
    e = 17
    # password = input("Enter the code: ").upper()
    # digits = int(input("Enter the number the digits: "))
    # n = int(input("Enter value of 'n': "))
    # e = int(input("Enter value of 'e': "))

    lenPass = len(password)
    rem = lenPass % digits
    if rem != 0:
        password += " " * (rem - 1)
        lenPass = len(password)

    Mi = []
    div = lenPass // digits
    # print("Mi")
    for i in range(div):
        index = i * digits
        val = password[index : index + digits]

        M = ""
        for j in val:
            value = code.get(j)
            diff = digits - len(value)
            if diff != 0:
                value = "0" * diff + value
            M += value
        # print(M)
        Mi.append(int(M))

    Ci = ""
    # print("Ci")
    for i in range(len(Mi)):
        C = str((Mi[i] ** e) % n)
        diff = digits * 2 - len(C)
        C = "0" * diff + C
        Ci += C
        # print(C)

    print("Encrypted code is: ", Ci)
    return Ci


def decryption(password):
    dec = ""
    Mi = []

    digits = 2
    d = 157
    n = 2773
    # digits = int(input("Enter the number the digits: "))
    # n = int(input("Enter value of 'n': "))
    # d = int(input("Enter value of 'd': "))

    digit_sqr = digits * digits
    loop = len(password) // digit_sqr
    for i in range(loop):
        index = i * digit_sqr
        Ci = int(password[index : index + digit_sqr])
        # print("Ci: ", Ci)
        # val = str(val[-digits * digits:])
        M = str((Ci ** d) % n)
        diff = digit_sqr - len(M)
        if diff != 0:
            M = "0" * diff + M
        # print("Mi: ", M)

        for j in range(digits):
            value = M[j * digits : digits * (j + 1)]
            if len(value) > 2:
                value = value[-2:]
            Mi.append(value)

    for i in range(len(Mi)):
        dec += get_key(Mi[i])

    print("Decrypted Code is: ", dec)
    return dec




global code
code = {"A": "00", "B": "01", "C": "02", "D": "03", "E": "04", "F": "05", "G": "06", "H": "07", "I": "08", "J": "09",
        "K": "10", "L": "11", "M": "12", "N": "13", "O": "14", "P": "15", "Q": "16", "R": "17", "S": "18", "T": "19",
        "U": "20", "V": "21", "W": "22", "X": "23", "Y": "24", "Z": "25", " ": "26"}


key1 = encryption()
key2 = decryption(key1)
