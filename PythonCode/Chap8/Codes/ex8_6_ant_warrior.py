n = int(input())

arr = list(map(int, input().split()))

# 각 위치부터 방문을 시작했을 때 구할 수 있는 식량의 최댓값 저장
arr2 = [0] * n

for i in range(n):
    # 현재 위치에서 얻을 수 있는 식량
    curIndex = i
    arr2[i] = arr[i]

    maxIndex = 0
    maxVal = 0
    for j in range(n):
        if j == i or abs(i-j) == 1:
            continue
        if arr[maxIndex] < arr[j]:
            maxIndex = j
            maxVal = max[j]

    arr2[i] += maxVal


print(max(arr2))
