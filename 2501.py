divisor = list()
a, b = map(int, input().split())

for i in range(a):
    if a%(i+1) == 0:
        divisor.append(i+1)

if len(divisor) < b:
    print(0)
else:
    print(divisor[b-1])