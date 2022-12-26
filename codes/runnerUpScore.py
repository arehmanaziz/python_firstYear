# scores = [7, 8, -10, 3, 9, 5, 5, 2, 9, 6]
scores = [1, -1, -2, -1]

# 1st method

# set will remove repeating values
setScores = set(scores)
listScores = sorted(list(setScores))
if len(listScores) > 1:
    # list can't be sort so we have to convert it into list
    runnerUp = listScores[-2]
else:
    runnerUp = listScores[0]
print(runnerUp)


# 2nd method

sortedScore = sorted(scores)
maxScore = sortedScore[-1]
runnerUp = sortedScore[0]
index = len(scores) - 2
if maxScore != runnerUp:
    while True:
        if sortedScore[index] != maxScore:
            runnerUp = sortedScore[index]
            break

        else:
            index -= 1

print(runnerUp)
