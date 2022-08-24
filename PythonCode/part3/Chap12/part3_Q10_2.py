def rotate(key, m):
    res = [[0]*3 for _ in range(m)]
    for i in range(m):
        for j in range(m):
            res[i][j] = key[m-j-1][i]
    return res


def move(key, d):  # 상, 하, 좌, 우, 0, 1, 2, 3
    if d == 0:
        return


def solution(key, lock):
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            return







key1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock1 = [[1,1,1], [1,1,0], [1,0,1]]

print(solution(key1, lock1))
