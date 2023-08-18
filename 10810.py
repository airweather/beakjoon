n, m = map(int, input().split())

basket = [0 for i in range(n)]

for i in range(m):
    i, j, k = map(int, input().split())
    for idx in range(len(basket)):
        if (idx >= i-1 and idx <= j-1):
            basket[idx] = k

print(' '.join(str(item) for item in basket))