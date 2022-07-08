data = input()

row = int(data[1])
col = int(ord(data[0])) - int(ord('a')) + 1

# 나이트가 움직일 수 있는 경우의 수
steps = [ (-2, -1), (-2, 1), (2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2) ]

res = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <=8:
        res += 1

print(res)