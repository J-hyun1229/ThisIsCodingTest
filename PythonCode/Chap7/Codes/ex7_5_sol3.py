#  집합 자료형을 이용한 풀이(교재 7-7.py)

n = int(input())
arr = set(map(int, input().split()))  # 매장의 재고 목록을 set 자료형으로 저장.

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in arr:
        print("yes", end=' ')
    else:
        print("no", end=' ')

