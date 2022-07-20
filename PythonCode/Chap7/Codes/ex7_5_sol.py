# 이진탐색을 이용한 풀이.

def bin_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1

    return None


n = int(input())

arr = list(map(int, input().split()))
arr.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    res = bin_search(arr, i, 0, n-1)
    if res != None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
