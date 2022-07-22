x = int(input())
d = [0] * 30001
d[1] = 0


def make_one(arr, x):

    for i in range(2, x+1):
        # 1을 빼는 경우부터 시작
        arr[i] = arr[i-1] + 1  # 1을 빼는 연산을 한번 헀으므로 횟수 +1

        if i%5 == 0:
            arr[i] = min(arr[i], arr[i//5]+1)

        if i%3 == 0:
            arr[i] = min(arr[i], arr[i//3]+1)

        if i%2 == 0:
            arr[i] = min(arr[i], arr[i//2]+1)  # arr[i//2] + 1 -> 나누기 연산을 했으므로 횟수 +1

    return arr[x]


res = make_one(d, x)
print(res)
