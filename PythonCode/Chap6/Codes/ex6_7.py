import random

arr = []
for i in range(10):
    arr.append(random.randrange(0, 9))

res = sorted(arr)
arr.sort()
print(arr)
print(res)
