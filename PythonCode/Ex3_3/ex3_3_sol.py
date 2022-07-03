# 교재 답안을 참고하여 개선한 코드

n, m = map(int, input().split())

res = 0

for i in range(0, n) :
    data = list(map(int, input().split()))
    min_value = min(data) # min(): 전달받은 인자 내에서 최솟값을 찾아 리턴
    res = max(res, min_value) # max(): 전달받은 인자 내에서 최댓값을 찾아 리턴

print(res)