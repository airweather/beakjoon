receipt = int(input())
count = int(input())

total = 0

for i in range(count):
    a, b = map(int, input().split())
    total += a * b
    
if(receipt == total):
    print("Yes")
else:
    print("No")