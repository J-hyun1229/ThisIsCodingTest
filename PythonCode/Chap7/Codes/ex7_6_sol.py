n, m = map(int, input().split())  # 떡 개수, 요청 길이. 적어도 m만큼의 길이를 가져가야 함.

arr = list(map(int, input().split()))

length = 0

start = 0
end = max(arr)
res = 0

while start <= end:
    length = 0  # 손님이 가져갈 수 있는 떡의 길이
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            length += (i-mid)

    if length < m:
        end = mid-1
    else:
        res = mid
        start = mid+1

print(res)
