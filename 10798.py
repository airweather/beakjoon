inputList = []

for i in range(5):
    inputList.append(list(input()))

reversedList = ""
for i in range(5):
    newList = []
    for j in range(len(inputList[i])):
        reversedList = reversedList + (inputList[j][i])

print(reversedList)