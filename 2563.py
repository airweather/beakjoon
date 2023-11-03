# paper= [[0] * 100 for _ in range(100)]

# for _ in range(int(input())):
#     a, b = map(int, input().split(" "))
#     for i in range(100):
#         if a+(i//10)-1 < 100 and b+(i%10) < 100:
#             paper[a+(i//10)-1][b+(i%10)-1] = 1
         
# count = 0

# for i in range(100):
#     for j in paper[i]:
#         if j == 1:
#             count += 1
            
# print(count)

paper = [[0] * 100 for _ in range(100)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            if 0 <= a + i < 100 and 0 <= b + j < 100:
                paper[a + i][b + j] = 1

count = sum(row.count(1) for row in paper)

print(count)