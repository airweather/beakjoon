total = int(input())
numList = list(map(int, input().split()))
target = int(input())
counter = 0


for item in numList:
    if(item == target):
        counter += 1

print(counter)