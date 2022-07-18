# 선택 정렬 - i번째 원소와 i번째로 작은 원소의 위치를 바꾸면서 정렬.

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]  # 스와프. tmp가 필요 없다.

print(arr)
