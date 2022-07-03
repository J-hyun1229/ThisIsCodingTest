arr1 = input().split()
n,m,k=0,0,0

n = int(arr1[0])
m = int(arr1[1])
k = int(arr1[2])

arr2 = input().split()
for i in range(0, len(arr2)):
    arr2[i] = int(arr2[i])


arr2.sort()
arr2.reverse()

res = 0
count = 0

for i in range(0, m):
    # 같은 수가 3번 더해지면 두번째로 큰 수를 더하고 count 초기화
    if count == 3 :
        res += arr2[1]
        count = 0
    # 같은수가 더해진 횟수가 3번 이하라면 가장 큰 수 더함
    else :
        res += arr2[0]
        count += 1

print(res)