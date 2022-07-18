import random

arr = []
for i in range(10):
    arr.append(random.randrange(0, 9))

print("정렬 전 리스트: ", arr)

count = [0] * (max(arr) + 1)

for i in range(len(arr)):
    count[arr[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

