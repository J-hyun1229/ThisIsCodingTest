def go_r(li, k) :
    if li[1] < k:
        li[1] += 1

def go_l(li, k):
    if li[1] > 1:
        li[1] -= 1

def go_u(li, k):
    if li[0] > 1:
        li[0] -= 1

def go_d(li, k):
    if li[0] < k:
        li[0] += 1



n = int(input())

# print(n)

plan = input().split()

# print(plan)

cur = [1,1]

for p in plan:
    if p == 'R':
        go_r(cur, n)
    elif p == 'L':
        go_l(cur, n)
    elif p == 'U':
        go_u(cur, n)
    elif p == 'D' :
        go_d(cur, n)
    else:
        print("유효하지 않은 인자 포함")

for i in cur:
    print(i, end=' ')