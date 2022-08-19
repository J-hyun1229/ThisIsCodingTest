# 동전 개수
n = int(input())

coins = list(map(int, input().split()))
coins.sort(reverse=True)

# print(coins)

res = 1

while True:
    tmp = res
    for coin in coins:
        if (tmp > coin) or (tmp-coin == 0):
            tmp -= coin
            # print(tmp)

    if tmp != 0:
        break

    res += 1

print(res)
