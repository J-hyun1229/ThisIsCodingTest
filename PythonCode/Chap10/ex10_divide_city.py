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


# 집의 개수, 길의 개수
n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edges = []

for i in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
include_edges = []  # 최소신장트리에 포함되는 간선
res = 0  # 구할 최솟값

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        include_edges.append(edge)
        res += cost

res -= max(include_edges)[0]

print(res)
