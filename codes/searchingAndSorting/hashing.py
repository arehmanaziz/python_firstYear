def hashingIndex(seatNumber):
    index = int(seatNumber[-3:])
    return index


def sortingByHashMethod(data):
    numOfStudents = len(data)
    indexData = []
    for i in range(numOfStudents):
        indexData.append(int(data[i][-3:]))
    maxNumber = max(indexData) + 1

    sn = []
    for j in range(maxNumber):
        sn.append("")

    for k in range(numOfStudents):
        index = hashingIndex(data[k])
        sn[index] = data[k]

    return sn
    

seatNumbers = ["B20102009", "B20102999", "B20102001", "B20102000", "B20102019"]
sortNumbers = sortingByHashMethod(seatNumbers)
print(sortNumbers)
    