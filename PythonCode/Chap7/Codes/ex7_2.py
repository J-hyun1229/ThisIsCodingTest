# 재귀 호출을 이용한 이진 탐색

def binary_search_recur(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search_recur(array, target, start, mid-1)
    else:  # 찾으려는 값이 중간값보다 크거나 찾으려는 값이 없는 경우
        return binary_search_recur(array, target, mid+1, end)


n, target = map(int, input().split())

arr = list(map(int, input().split()))

res = binary_search_recur(arr, target, 0, n-1)

if res == None:
    print("원소가 존재하지 않습니다.")
else:
    print(res + 1)
