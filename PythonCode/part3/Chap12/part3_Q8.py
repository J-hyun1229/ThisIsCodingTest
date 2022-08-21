import heapq

# 문자열 s는 대문자, 숫자로만 구성된다.
s = input()

sumVal = 0
q = []

for ch in s:
    if 'A' <= ch <= 'Z':
        heapq.heappush(q, ch)
    else:
        sumVal += int(ch)


while q:
    print(heapq.heappop(q), end='')

print(sumVal)
