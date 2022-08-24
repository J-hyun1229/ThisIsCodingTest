def rotate(key, m):
    res = [[0] * 3 for _ in range(m)]
    for i in range(m):
        for j in range(m):
            res[i][j] = key[m - j - 1][i]
    return res


def move(key, d):  # 상, 하, 좌, 우, 0, 1, 2, 3
    if d == 0:
        return


def solution(key, lock):
    one_of_key = []  # (1, 0), (2, 1), (2, 2)
    one_of_lock = []  # (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (2, 0), (2, 2)
    zero_of_lock = []  # (1, 2), (2, 1)
    # 열쇠의 돌기 위치
    for i in range(len(key)):
        for j in range(len(key[0])):
            if key[i][j] == 1:
                one_of_key.append((i, j))

    # 자물쇠의 홈, 돌기 위치
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            if lock[i][j] == 1:
                one_of_lock.append((i, j))
            else:
                zero_of_lock.append((i, j))

    if len(one_of_key) < len(zero_of_lock):
        return False
    # print("one of key:", one_of_key)
    # print("one of lock:", one_of_lock)
    # print("zero of lock:", zero_of_lock)
    # return
    res = True  # 리턴할 결과
    for i in range(4):
        print("i = ", i)
        print("one of key:", one_of_key)
        print("one of lock:", one_of_lock)
        print("zero of lock:", zero_of_lock)
        res = True
        # 열쇠 1과 자물쇠 0의 인덱스 차이가 모두 같아야 함.
        diff_match_row = zero_of_lock[0][0] - one_of_key[0][0]
        diff_match_col = zero_of_lock[0][1] - one_of_key[0][1]
        for a in range(len(zero_of_lock)):
            if (zero_of_lock[a][0] - one_of_key[a][0]) != diff_match_row:
                print("res is False:", zero_of_lock[a], "and", one_of_key[a], "is mismatch")
                print("zero of lock - one of key =", zero_of_lock[a][0] - one_of_key[a][0], ",intedned", diff_match_row)
                res = False
                break
            if (zero_of_lock[a][1] - one_of_key[a][1]) != diff_match_col:
                print("res is False:", zero_of_lock[a], "and", one_of_key[a], "is mismatch")
                print("zero of lock - one of key =", zero_of_lock[a][1] - one_of_key[a][1], ",intedned", diff_match_col)
                res = False
                break

            # 열쇠 1과 자물쇠 1의 인덱스는 모두 달라야 함.
            for b in range(len(one_of_key)):
                if (one_of_lock[b][0] - one_of_key[b][0]) == diff_match_row \
                        and (one_of_lock[b][1] - one_of_key[b][1]) == diff_match_col:
                    res = False
                    break

        # 가능한 경우 탐색 중지.
        if res is True:
            break

        # 열쇠를 돌리고 열쇠 돌기 위치를 다시 구함.
        key = rotate(key, len(key))
        one_of_key = []
        for x in range(len(key)):
            for y in range(len(key[0])):
                if key[x][y] == 1:
                    one_of_key.append((x, y))

    return res


key1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key1, lock1))
