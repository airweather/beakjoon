a, b = map(int, input().split())

arr = [int(num) for num in list(input().split())]
arr.sort(reverse=True)

print(arr[b-1])