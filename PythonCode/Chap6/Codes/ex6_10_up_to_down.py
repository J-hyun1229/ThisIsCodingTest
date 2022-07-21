n = int(input())

arr = []

for i in range(n):
    arr.append(int(input()))

arr.sort()  # O(n) = nlog(n) 퀵 + 병합정렬 -> 하이브리드 정렬 방식
arr.reverse()

for i in arr:
    print(i, end=' ')
