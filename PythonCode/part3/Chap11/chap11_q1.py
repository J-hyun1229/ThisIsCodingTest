# 모험가 수
n = int(input())

arr = list(map(int, input().split()))

arr.sort()

res = 0

i = 0
flag = False

while i < n:
    for j in range(i, i+arr[i]):
        # print("for %d in range (%d, %d)" % (j, i, i + arr[i]))
        if arr[j] > arr[i]:
            # print("if %d > %d: " % (arr[j], arr[i]))
            flag = True
            break

    if flag:
        # print("if flag activated")
        break

    # print("i = %d + %d" % (i, arr[i]))
    i += arr[i]
    res += 1
    # print("i = %d" % i)

print(res)
