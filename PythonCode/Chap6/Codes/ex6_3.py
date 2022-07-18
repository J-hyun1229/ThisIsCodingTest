arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):  # 자신의 왼쪽 방향으로 탐색 시작.
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:  # 자신보다 작은 요소를 찾으면 멈춤. 그 앞은 정렬되어있다고 간주.
            break

print(arr)
