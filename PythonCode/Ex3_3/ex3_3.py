n, m = map(int, input().split())

arr = []

for i in range(0, n):
    arr.append(list(map(int, input().split())))

#print(arr)

for i in range(0, n):
    arr[i].sort()

res = -1

for i in range(0, n):
    tmp = arr[i][0]
    if res < tmp:
        res = tmp

print(res)