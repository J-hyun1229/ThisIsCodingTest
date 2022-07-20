n, m = map(int, input().split())  # 떡 개수, 요청 길이. 적어도 m만큼의 길이를 가져가야 함.

arr = list(map(int, input().split()))

arr2 = [0] * n

length = 0

while True:
    for i in range(n):
        if arr[i] >= length:
            arr2[i] = arr[i]-length
        else:
            arr2[i] = 0

    total = sum(arr2)
    if total > m:
        length += 1
    elif total == m:
        break
    else:
        length -= 1
        break

print(length)
