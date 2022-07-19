# 반복문을 이용한 이진 탐색

def binary_search_rep(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n, target = map(int, input().split())

arr = list(map(int, input().split()))

res = binary_search_rep(arr, target, 0, n-1)

if res is None:
    print("원소를 찾을 수 없습니다.")
else:
    print(res + 1)
