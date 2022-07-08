# 맵의 가로, 세로 크기
n, m = map(int, input().split())

# 좌표, 방향
a, b, d = map(int, input().split())

# 방향 [북, 동, 남, 서]
ds = [0, 1, 2, 3]

# 각 방향을 보고 있을 때 움직임
dsMove = [(-1, 0), (0, 1), (1, 0), (0, -1)]

arr = []

res = 0

for i in range(n):
    arr.append(input().split())

moved = False

i = 0

num = 0

arr[a][b] = 2

while True:
    moved = False
    # 방향 전환(왼쪽으로 90도)
    if d == 0:
        d = 3
    else:
        d -= 1
        
    # 해당 방향으로 이동시 좌표 구하기
    atmp = a + dsMove[d][0]
    btmp = b + dsMove[d][1]

    # 좌표가 맵 내부일 경우
    if atmp >= 0 and btmp >= 0:
        # 좌표가 맵 내부이고 육지일 경우
        if arr[atmp][btmp] == '0':
            a = atmp
            b = btmp
            moved = True
            i = 0
            res += 1
            arr[atmp][btmp] = '2'
    else:
        continue

    if not moved:
        # 이동할 수 없어 뒤로 가는 경우
        if i == 3:
            atmp = a - dsMove[d][0]
            btmp = b - dsMove[d][1]
            if atmp >= 0 and btmp >= 0:
                if arr[atmp][btmp] == '0' or arr[atmp][btmp] == '2':
                    a = atmp
                    b = btmp
                    moved = True
                    res += 1
                    i = 0
                    arr[atmp][btmp] = '2'
                elif arr[atmp][btmp] == '1':
                    break
            else:
                break
        else:
            i += 1

    num += 1
    print("차시:",num,"방향:",d,"moved:",moved)
    print("현재 위치: (%d, %d)" % (a, b))
    for li in arr:
        for e in li:
            print(e, end=' ')
        print()
    print(res)


print(res)
