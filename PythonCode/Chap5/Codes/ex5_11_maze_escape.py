from collections import deque


def find_side(board, arr, r, c):
    global n, m
    # 아래, 오른쪽
    ds = [(1, 0), (0, 1)]
    for i in ds:
        rtmp = r + i[0]
        ctmp = c + i[1]
        if rtmp < 0 or ctmp < 0 or rtmp >= n or ctmp >= m:
            continue
        else:
            if board[rtmp][ctmp] == '1':
                arr[r][c].append((rtmp, ctmp))


def bfs(board, arr, r, c):
    global count, dx, dy
    queue = deque()
    queue.append((r, c))
    for tup in arr[r][c]:
        queue.append(tup)
    board[r][c] = '2'
    count += 1
    print("현재 좌표: (%d, %d) count= %d" % (r, c, count))
    while queue:
        tmp = queue.popleft()
        rtmp = tmp[0]
        ctmp = tmp[1]
        if rtmp == dx and ctmp == dy:
            count += 1
            print("현재 좌표: ", tmp, "count=", count)
            break
        if board[rtmp][ctmp] == '1':
            for tup in arr[rtmp][ctmp]:
                queue.append(tup)
            board[rtmp][ctmp] = '2'
            count += 1
            print("현재 좌표: ", tmp, "count=", count)


n, m = map(int, input().split())

board = []

# 미로 생성 (방문가능 1, 방문불가 0)
for i in range(n):
    board.append(list(input()))

r, c = 0, 0

dx, dy = n-1, m-1

# 인접 리스트 -> arr[x][y]는 (x, y)의 인접 노드들의 좌표를 저장한 리스트.
arr = []

for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i].append([])

for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            find_side(board, arr, i, j)

count = 0

bfs(board, arr, 0, 0)

""" 
q2 = deque()
q2.append([(1,1), (1,2), (1,3)])
while q2:
    print(q2.popleft())
"""
print(count)
