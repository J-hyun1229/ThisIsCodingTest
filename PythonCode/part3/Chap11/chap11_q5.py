# 공 개수, 공 무게
n, m = map(int, input().split())

bArr = list(map(int, input().split()))

for i in range(n):
    tmp = bArr[i]
    bArr[i] = (i+1, tmp)  # (번호, 무게)

# print(bArr)

res = 0

for i in range(n):
    for j in range(i+1, n):
        if bArr[i][1] != bArr[j][1]:  # 두 공의 무게가 다르면 +1.
            res += 1

print(res)
