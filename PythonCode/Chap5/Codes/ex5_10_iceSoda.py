def find_side(board, arr, r, c):
    global n, m
    # 위, 아래, 왼쪽, 오른쪽별 좌표 변화
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(4):
        rtmp = r + ds[i][0]
        ctmp = c + ds[i][1]
        if rtmp < 0 or ctmp < 0 or rtmp >= n or ctmp >= m:
            continue
        else:
            if board[rtmp][ctmp] == '0':
                arr[r][c].append((rtmp, ctmp))


def dfs(arr, r, c, board):
    # 틀의 숫자를 2로 바꿔서 방문 처리
    board[r][c] = '2'
    # for문의 i는 인접 리스트 요소.
    for i in arr[r][c]:
        if board[i[0]][i[1]] == '0':
            dfs(arr, i[0], i[1], board)


n, m = map(int, input().split())

visited = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i].append(False)

# 얼음 틀
board = []

for i in range(n):
    board.append(list(input()))

# 인접 리스트 - 각 노드에 인접한 노드들의 배열 저장. 각 노드는 좌표로 표현
arr = []

# 인접 리스트 초기화
for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i].append([])

# 각 노드에 대한 인접 리스트 생성
for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            find_side(board, arr, i, j)

# 제출할 정답
count = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == '0':
            count += 1
            dfs(arr, i, j, board)

print(count)


""" test Code
for tmpStr in board:
    for index in range(len(tmpStr)):
        print(tmpStr[index], end = ' ')
    print()
"""

""" test Code
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()
"""