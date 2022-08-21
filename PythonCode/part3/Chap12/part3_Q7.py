# 자릿수는 항상 짝수
n = list(input())

# print(n) # n은 리스트.

length = len(n)
res = 0

for i in range(length//2):
    res += int(n[i])  # 앞에 반은 더함
    res -= int(n[-(i+1)])  # 뒤에 반은 뻄

if res == 0:
    print("LUCKY")
else:
    print("READY")