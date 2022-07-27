n = int(input())

# N * 2 크기의 바닥을 채우는 경우의 수
# 1 * 2, 2 * 1, 2 * 2 크기의 타일 존재.

res = 1

tmp = n//2
for i in range(tmp):
    res *= 3

if n%2 == 1:
    res += n - (n//2)


print(res % 796796)
