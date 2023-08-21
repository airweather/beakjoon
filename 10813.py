n, m = map(int, input().split())

basket = [i+1 for i in range(n)]

for i in range(m):
    i, j = map(int, input().split())
    i = i-1
    j = j-1
    basket[i], basket[j] = basket[j], basket[i]

print(" ".join(map(str, basket)))