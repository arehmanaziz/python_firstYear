# #     # Use the formula 2 ^ r >= m + r + 1
# #     # to calculate the no of redundant bits.
# #     # Iterate over 0 .. m and return the value
# #     # that satisfies the equation
# #
# #     for i in range(l):
# #         if (2 ** i >= l + i + 1):
# #             return i
# #
# #
# # def posRedundantBits(data, r):
# #     # Redundancy bits are placed at the positions
# #     # which correspond to the power of 2.
# #     j = 0
# #     k = 1
# #     m = len(data)
# #     res = ''
# #
# #     # If position is power of 2 then insert '0'
# #     # Else append the data
# #     for i in range(1, m + r + 1):
# #         if (i == 2 ** j):
# #             res = res + '0'
# #             j += 1
# #         else:
# #             res = res + data[-1 * k]
# #             k += 1
# #
# #     # The result is reversed since positions are
# #     # counted backwards. (m + r+1 ... 1)
# #     return res[::-1]
# # MSG='1011001'
# # l=len(MSG)
# r=4
# # t=posRedundantBits(MSG,r)
# # print(r)
# # print(t)
# MSG=[1,0,1,1,0,0,1]
#
# l=len(MSG)
#
#
#     # The result is reversed since positions are
#     # counted backwards. (m + r+1 ... 1)
#
#
# # l=len(MSG)
# # j = 0
# # k = 1
# # res = ''
# # for i in range(1, l + r  ):
# #
# #     if (i == 2 ** j):
# #         s=MSG[::i]
# #         print(s)
# #         t=sum(s)/2
# #         print(t)
# #         if t % 2 == 0:
# #             print("Here 1")
# #             res = res + '1'
# #             j += 1
# #         else:
# #             print("here zero")
# #             res = res + '0'
# #             j += 1
# #     else:
# #         print(res)
# #         res = res + str(MSG[-1 * k])
# #         k += 1
# # print(res)
option = int(input(
    'Press 1 for generating hamming code  \nPress 2 for finding error in hamming code\n\t Enter your choice:--\n'))

if (option == 1):  # GENERATE HAMMING CODE
    print('Enter the data bits')
    d = input()
    data = list(d)
    # print(data)
    data.reverse()
    # print(data)
    c=0
    ch=0
    j=0
    r=0
    h = []

    while ((len(d) + r + 1) > (2**r)):
        r = r + 1

    for i in range(0, (r + len(data))):
        p = (2 ** c)

        if (p == (i + 1)):
            h.append(0)
            c = c + 1

        else:
            h.append(int(data[j]))
            j = j + 1

    for parity in range(0, (len(h))):
        ph = (2 ** ch)
        if (ph == (parity + 1)):
            startIndex = ph - 1
            i = startIndex
            toXor = []

            while (i < len(h)):
                block = h[i:i + ph]
                toXor.extend(block)
                print(toXor)
                i += 2 * ph

            for z in range(1, len(toXor)):
                h[startIndex] = h[startIndex] ** toXor[z]
            ch += 1

    h.reverse()
    print('Hamming code generated would be:- ', end="")
    print (h)


elif (option == 2):  # DETECT ERROR IN RECEIVED HAMMING CODE
    print('Enter the hamming code received')
    d = input()
    data = list(d)
    data.reverse()
    c, ch, j, r, error, h, parity_list, h_copy = 0, 0, 0, 0, 0, [], [], []

    for k in range(0, len(data)):
        p = (2 ** c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if (p == (k + 1)):
            c = c + 1

    for parity in range(0, (len(h))):
        ph = (2 ** ch)
        if (ph == (parity + 1)):

            startIndex = ph - 1
            i = startIndex
            toXor = []

            while (i < len(h)):
                block = h[i:i + ph]
                toXor.extend(block)
                i += 2 * ph

            for z in range(1, len(toXor)):
                h[startIndex] = h[startIndex] ^ toXor[z]
            parity_list.append(h[parity])
            ch += 1
    parity_list.reverse()
    error = sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))

    if ((error) == 0):
        print('There is no error in the hamming code received')

    elif ((error) >= len(h_copy)):
        print('Error cannot be detected')

    else:
        print('Error is in', error, 'bit')

        if (h_copy[error - 1] == '0'):
            h_copy[error - 1] = '1'

        elif (h_copy[error - 1] == '1'):
            h_copy[error - 1] = '0'
            print('After correction hamming code is:- ')
        h_copy.reverse()
        print(int(''.join(map(str, h_copy))))

else:
    print('Option entered does not exist')