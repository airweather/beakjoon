numList = list()

for _ in range(9):
    line = input()
    text = line.split()

    number = [int(i) for i in text]
    numList = numList + number

maxNum = max(numList)

maxIdx = numList.index(maxNum)

print(maxNum)
print(maxIdx//9+1, maxIdx%9+1)