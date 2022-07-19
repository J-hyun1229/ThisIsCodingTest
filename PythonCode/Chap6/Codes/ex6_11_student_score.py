n = int(input())

arr = []

for i in range(n):
    data = input().split()
    name, score = data[0], data[1]
    arr.append((name, int(score)))


def score(info):
    return info[1]


res = sorted(arr, key=score)

for i in res:
    print(i[0], end=' ')

