records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# records = [["harry", 37.21], ["berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]

""""
sorted function sort a nested list w.r.t 1st value
to sort according to score
changing position of score
"""
# sortedRecord = sorted([[j, i] for i, j in records])
# print(sortedRecord)
#
# # 2nd lowest scorers record
secondLowest = []
# # the lowest score
# lowest = sortedRecord[0][0]
#
# i = 1
# while i < len(records):
#     score = sortedRecord[i][0]
#     if score != lowest:
#         secondLowest.append(sortedRecord[i][1])
#         break
#     i += 1
#
# # checking if there are multiple same scores
# if sortedRecord[i+1][0] == score:
#     try:
#         while (i < len(sortedRecord)) and (sortedRecord[i+1][0] == score):
#             secondLowest.append(sortedRecord[i+1][1])
#             i += 1
#     except IndexError:
#         pass

scores = sorted(list(set(x[1] for x in records)))
secondLowestScore = scores[1]

for i in range(1, len(records)):
    if records[i][1] == secondLowestScore:
        secondLowest.append(records[i][0])
        
secondLowest.sort()
for name in secondLowest:
    print(name)