a = "hh1h001h1101010h011"
length = len(a)
num = 5
c = 0
ch = 0
for i in range(length):
    parityIndex = 2 ** c - 1
    if i == parityIndex:
        startIndex = parityIndex
        i = startIndex
        toXor = []

        while i < length:
            block = a[i:i + parityIndex + 1]
            toXor.extend(block)
            i += 2 * (parityIndex + 1)

        for z in range(1, len(toXor)):
            a[startIndex] = str(int(a[startIndex]) ** int(toXor[z]))
        ch += 1

print(a)




