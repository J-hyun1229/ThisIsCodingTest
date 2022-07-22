x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    # 1을 빼는 경우
    d[i] = d[i-1] + 1