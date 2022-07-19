n, k = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

for i in range(k):
    minIndex = 0
    maxIndex = 0
    for j in range(n):
        if arr1[minIndex] > arr1[j]:
            minIndex = j

        if arr2[maxIndex] < arr2[j]:
            maxIndex = j

    if arr1[minIndex] < arr2[maxIndex]:
        arr1[minIndex], arr2[maxIndex] = arr2[maxIndex], arr1[minIndex]

res=0
for i in arr1:
    res += i

print(res)