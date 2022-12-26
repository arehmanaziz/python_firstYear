# ERROR CORRECTION (ONLY FOR 1 BIT ERROR) by ABDUR REHMAN AZIZ
# =======================================

# keep taking bits as input from user and store them in a list
# stop and return the BITS LIST if a number other than 0 or 1 is entered as input
def bits():
    code = []
    while True:
        bit = int(input("Enter the value of bit: "))
        if bit != 0 and bit != 1:
            break
        code.append(bit)

    return code


# Display the bits, stored in a list, together in a single line
def bitsDisplay(bitsList):
    length = len(bitsList)
    string = ""
    for i in range(length):
        string += str(bitsList[i])
    return string


# calculate and return that how many HAMMING BITS should be placed
def numberOfHammingBits(message):
    messageLength = len(message)
    for parityBit in range(messageLength):
        if (2 ** parityBit) >= (messageLength + parityBit + 1):
            return parityBit


# placing -1 at the place of hamming bits at position 2^i ; where i = 0,1,2......
def placeHammingBits(message, numOfHammingBits):
    for i in range(numOfHammingBits):
        message.insert((2 ** i - 1), -1)
    return message


# finding the values of hamming bits
def hammingBitsValues(message, numOfHammingBits):
    # Select a parity scheme, either EVEN or ODD
    scheme = int(input("""
    Please choose a parity scheme
    Even = 1
    Odd = 2
    
    Your Choice: """))
    while scheme != 1 and scheme != 2:
        scheme = int(input("Please choose a valid option (1 or 2): "))

    # slicing all the bits according to the position of hamming bits
    messagePacket = separateListsForHammingBits(message, numOfHammingBits)

    length = len(messagePacket)
    if scheme == 1: # if EVEN
        for i in range(length):
            val = sum(messagePacket[i]) + 1
            if val % 2 == 0:  # means It's even, so we'll place 0 in its place
                message[2 ** i - 1] = 0
            else: # means It's odd, so we'll place 1 in its place
                message[2 ** i - 1] = 1
    else: # if ODD
        for i in range(length):
            val = sum(messagePacket[i]) + 1
            if val % 2 == 1: # means It's odd, so we'll place 0 in its place
                message[2 ** i - 1] = 0
            else: # means It's even, so we'll place 1 in its place
                message[2 ** i - 1] = 1

    # returning parity scheme, and bits with the values of hamming bits
    return message, scheme


# slice qll the bits according to the position of Hamming bits and assign them in a separate list
# e.g for Hamming Bit 2 we'll select bits of positions: 2,3,6,7,10,11....
# e.g for Hamming Bit 3 we'll select bits of positions: 3,4,5,9,10,11....
def separateListsForHammingBits(message, numOfHammingBits):
    messagePacket = []
    for i in range(numOfHammingBits):
        messageList = []
        length = len(message)
        j = 2 ** i - 1 # start from the position of the hamming bit
        k = j + 2 ** i
        if k <= length:
            while k <= length:
                for val in range(j, k):
                    messageList.append(message[val])
                j = k + 2 ** i
                k = j + 2 ** i
        else: # run loop till the last value
            for val in range(j, length):
                messageList.append(message[val])

        messagePacket.append(messageList)

    # returning list of lists
    return messagePacket


# check whether the message contains an error bit or not
# if does, it'll correct it
def checkReceivedMessage(message, messagePacket, scheme):
    length = len(messagePacket)
    errorIndexList = []
    error = False
    errorIndex = None
    if scheme == 1: # if EVEN
        # sum of all the values inside the HammingBitList should be EVEN, if not, it has an ERROR
        for i in range(length):
            val = sum(messagePacket[i])
            if val % 2 != 0: # means it has an ERROR
                errorIndexList.append(2 ** i)
    else: # if ODD
        # sum of all the values inside the HammingBitList should be ODD, if not, it has an ERROR
        for i in range(length):
            val = sum(messagePacket[i])
            if val % 2 != 1: # means it has an ERROR
                errorIndexList.append(2 ** i)

    if errorIndexList:  # if not empty (there's an ERROR in the received message)
        error = True
        errorIndex = sum(errorIndexList) - 1 # Index of the ERROR BIT
        # if ERROR BIT == 1, replace it with "0" or vice versa
        if message[errorIndex] == 1:
            message[errorIndex] = 0
        else:
            message[errorIndex] = 1

    return message, error, errorIndex


# removes hamming bits of received message
def removeHammingBits(message, numOfHammingBits):
    for i in range(numOfHammingBits):
        index = numOfHammingBits - i - 1
        message.pop(2 ** index - 1)
    return message

# Ask to input message in bits that we have to send
# Add Hamming Bits in the message
def senderSideProcess():
    # inputMessage = bits()
    inputMessage = [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1]
    print(f"Entered Message: {bitsDisplay(inputMessage)}")
    # finding how many hamming bits should be placed in the message
    hammingBits = numberOfHammingBits(inputMessage)
    # placing -1 at the place of hamming bits
    messageWithHammingBits = placeHammingBits(inputMessage, hammingBits)
    # finding the values of hamming bits then replacing them with -1 at their respective positions
    finalMessage, scheme = hammingBitsValues(messageWithHammingBits, hammingBits)

    print(f"Sent Message: {bitsDisplay(finalMessage)}")
    return finalMessage, scheme



def receiverSideProcess(receivedMessage, scheme):
    # receivedMessage = bits()
    # we have to enter the parity scheme and the bits that we  received,
    # but here we are taking the same message as parameter for ease

    # we know that the message we took as parameter will not contain any error
    # that's why we're entering a false bit in the line below (you can change this value if you want)
    receivedMessage[13] = 0
    print(f"Received Message: {bitsDisplay(receivedMessage)}")

    """
    scheme = int(input("
    Please choose a parity scheme
    Even = 1
    Odd = 2

    Your Choice: "))
    while scheme != 1 and scheme != 2:
        scheme = int(input("Please choose a valid option (1 or 2): "))"""

    # finding number of hamming bits that are placed in the given message
    hammingBits = 0
    while True:
        try:
            index = 2 ** hammingBits - 1
            check = receivedMessage[index]
            hammingBits += 1
        except IndexError:
            break

    # slicing all the bits according to the position of hamming bits
    messagePacket = separateListsForHammingBits(receivedMessage, hammingBits)
    # checking if the received message contains an error or not
    correctMessage, error, position = checkReceivedMessage(receivedMessage, messagePacket, scheme)
    if error: # if there's an error in the received message
        print(f"There was an error in the received message at Position {position + 1}, we've corrected it")
        print(f"Corrected Message: {bitsDisplay(correctMessage)}")
    # removing hamming bits
    finalMessage = removeHammingBits(correctMessage, hammingBits)
    print(f"Decoded Message: {bitsDisplay(finalMessage)}")

    return finalMessage


sentMessage, parityScheme = senderSideProcess()
decodeMessage = receiverSideProcess(sentMessage, parityScheme)














