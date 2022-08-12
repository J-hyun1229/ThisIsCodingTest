def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, node1, node2):
    node1 = find_parent(parent, node1)
    node2 = find_parent(parent, node2)
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2


v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

isCycle = False

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent, b):
        isCycle = True
        break
    else:
        union_parent(parent, a, b)

if isCycle:
    print("사이클 발생")
else:
    print("사이클 없음")
