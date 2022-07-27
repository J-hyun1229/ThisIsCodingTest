n, m = map(int, input().split())

res = 0

coins = []
for i in range(n):
    coins = int(input())

tmp = m
for coin in coins:
    tmp %= coin

# 불가능한 경우
if tmp != 0:
    res = -1

# 가능할 경우
nums = []
# 각 화폐단위가 들어갈 수 있는 최대 단위
for coin in coins:
    nums.append(m//coin)

resList = []

tmpList = []
tmp = m
for i in range(nums[0]+1):
    tmpList.append(i)

resList.append(tmpList)



