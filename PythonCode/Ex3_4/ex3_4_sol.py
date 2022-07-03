# n를 k로 최대한 나누는 횟수
n, k = map(int, input().split())

count = 0

while True:
    maxVal = (n//k) * k
    count += (n - maxVal)
    
    n = maxVal
    if n < k:
        break

    count += 1
    n //= k

    print("in progress: %d" % count)

count += (n-1)

print(count)