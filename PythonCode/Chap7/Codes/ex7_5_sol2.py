# 계수정렬을 이용한 풀이 (교재 7-6.py)

n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())

x = list(map(int,input().split()))

for i in x:
    if array[i] == 1:  # 해당 부품이 존재함
        print("yes", end=' ')
    else:
        print("no", end=' ')

