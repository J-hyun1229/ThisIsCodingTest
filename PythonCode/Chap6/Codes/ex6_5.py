arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 피벗보다 작은 요소들의 리스트
    right_side = [x for x in tail if x > pivot]  # 피벗보다 큰 요소들의 리스트

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(arr))
