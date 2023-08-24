# n, m = map(int, input().split())

# firstMatrix = list()
# secondMatrix = list()

# sumMatrix = list()

# for _ in range(n):
#     firstMatrix.append(input().split())

# for _ in range(n):
#     secondMatrix.append(input().split())

# for i in range(n):
#     for j in range(m):
#         print(int(firstMatrix[i][j]) + int(secondMatrix[i][j]), end=" ")
#     print()

n, m = map(int, input().split())

first_matrix = [list(map(int, input().split())) for _ in range(n)]

second_matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    result_row = [str(first_matrix[i][j] + second_matrix[i][j]) for j in range(m)]
    print(" ".join(result_row))