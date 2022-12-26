def inputList():
    numOfValues = int(input("Enter number of values: "))
    values = []
    for i in range(numOfValues):
        value = float(input(f"Enter value {i + 1}: "))
        values.append(value)

    return values


def mergeSort(arr):
    if len(arr) > 1:
        breakPoint = len(arr)//2
        leftArray = arr[:breakPoint]
        rightArray = arr[breakPoint:]

        # Sort the two halves

        mergeSort(leftArray)
        mergeSort(rightArray)

        i = j = k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arr[k] = leftArray[i]
                i += 1
            else:
                arr[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arr[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arr[k] = rightArray[j]
            j += 1
            k += 1


# val = inputList()
val = [23, 34, 8, 1, 45, 92, 60, 71, 44, 9, 59]
mergeSort(val)
print(val)
