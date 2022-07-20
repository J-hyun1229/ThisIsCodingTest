def bin_search(array, target, start, end):
    if start > end:
        return False
    mid = (start+end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return bin_search(array, target, start, mid-1)
    else:
        return bin_search(array, target, mid+1, end)


n = int(input())  # 매장 부품 종류 수

nArr = list(map(int, input().split()))

m = int(input())  # 주문 부품 종류 수

mArr = list(map(int, input().split()))

nArr.sort()

count = 0

for target in mArr:
    res = bin_search(nArr, target, 0, n-1)
    if res is True:
        print("yes", end='')
    else:
        print("no", end='')
    print(' ', end='')
