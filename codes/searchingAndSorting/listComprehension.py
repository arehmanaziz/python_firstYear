i = [0, 1]
j = [0, 1]
k = [0, 1, 2]
n = 3

possibleOutcomes = [[x, y, z] for x in i for y in j for z in k if (x+y+z != n)]
print(possibleOutcomes)