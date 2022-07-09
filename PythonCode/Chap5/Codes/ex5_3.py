count = 0


def recursive_func():
    global count
    count += 1
    if count == 5:
        return
    print('재귀 함수를 호출합니다.')
    recursive_func()


recursive_func()