num = int(input())

for i in range(num):
    for j in range(num + i):
        if j < num - 1 - i:
            print(" ", end="")
        else:
            print("*", end="")
    print()

for i in range(num - 1):
    for j in range((num-1) * 2 - i):
        if j <= i:
            print(" ", end="")
        else:
            print("*", end="")
    print()

# for i in range(num):
#     print(" " * (num - 1 - i) + "*" * (num + i))

# for i in range(num - 1):
#     print(" " * (i + 1) + "*" * ((num - 1) * 2 - i))