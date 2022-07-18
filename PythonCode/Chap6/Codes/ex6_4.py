arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    if start >= end:  # 리스트 요소가 1개인 경우 종료
        return
    pivot = start
    left = start+1
    right = end
    while left <= right:
        while left <= end and array[left] <= array[pivot]:  # 리스트 왼쪽에서부터 피벗보다 큰 원소 검색
            left += 1
        while right > start and array[right] >= array[pivot]:  # 리스트 오른쪽부터 피벗보다 작은 원소 검색
            right -= 1

        if left > right:  # 왼쪽에서 찾은 요소(피벗보다 작은 요소)와 오른쪽에서 찾은 요소(피벗보다 큰 요소)가 엇갈릴 경우, 피벗과 작은 요소 교환.
            array[pivot], array[right] = array[right], array[pivot]
        else: # 엇갈리지 않았다면 큰 요소와 작은 요소 교환
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(arr, 0, len(arr)-1)

print(arr)
