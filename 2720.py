change = [25, 10, 5, 1]

# Greedy - coin change algorithm

# 첫번째 for 문
# test case 수

# 안쪽 for 문
# 4번

for i in range(int(input())):
    changeList = []
    money = int(input())
    for j in range(4):
        changeList.append(str(money // change[j]))
        money = money % change[j]
    print(' '.join(changeList))
