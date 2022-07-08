rows = [1, 2, 3, 4, 5, 6, 7, 8]
cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

str = input()

c = cols.index(str[0]) + 1
r = int(str[1])

count = 0

if r > 2: # 위로 두칸 가능
    if c > 1: # 위로 2, 왼쪽 1 가능
        count += 1
    if c < 8: # 위로 2, 오른쪽 1 가능
        count += 1

if r < 7: # 아래로 두칸 가능
    if c > 1: # 아래로 2, 왼쪽 1 가능
        count += 1
    if c < 8: # 아래로 2, 오른쪽 1 가능
        count += 1

if c > 2: # 왼쪽으로 두칸 가능
    if r > 1: # 왼쪽 2, 위로 1 가능
        count += 1
    if r < 8: # 왼쪽 2, 아래로 1 가능
        count += 1

if c < 7: # 오른쪽으로 두칸 가능
    if r > 1: # 오른쪽 2, 위로 1 가능
        count += 1
    if r < 8: # 오른쪽 2, 아래로 1 가능
        count += 1

print(count)
