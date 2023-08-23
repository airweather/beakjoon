k = int(input())

num = list()

for _ in range(k):
    inputNum = int(input())
    if inputNum==0:
        num.pop()
    else:
        num.append(inputNum)
        
print(sum(num))