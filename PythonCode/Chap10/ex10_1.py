def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    # 부모노드가 자기 자신이면 루트노드
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 더 작은 쪽이 부모노드
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드 개수, 간선 개수(union 연산 개수)
v, e = map(int, input().split())
parent = [0] * (v+1)

# 처음에는 모두 자기 자신을 부모노드로 설정.
for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

print("부모 테이블: ",end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

