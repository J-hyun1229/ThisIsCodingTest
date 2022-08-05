n, m = map(int, input().split())

d = [10001] * (m+1)

coins = []
for i in range(n):
    coins.append(int(input()))

d[0] = 0

for i in range(n):
    for j in range(coins[i], m+1):
        if d[j-coins[i]] != 10001:
            d[j] = min(d[j], d[j-coins[i]]+1)


print(d[m])
