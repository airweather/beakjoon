# t = int(input())

# for _ in range(t):
#     r, s = input().split()
#     for i in range(len(s)):
#         print(s[i]*int(r), end="")
#     print()

t = int(input())

for _ in range(t):
    r, s = input().split()
    result = ''.join([char * int(r) for char in s])
    print(result)