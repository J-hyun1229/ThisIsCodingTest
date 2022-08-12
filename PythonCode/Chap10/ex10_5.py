def find_parent(parent, node):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, node1, node2):
    # node1과 node2의 루트 노드를 찾아서 저장.
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

# 모든 간선을 담을 리스트
edges = []
# 최소 신장 트리 비용
res = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    # 두 노드와 비용을 튜플로 저장.
    edges.append((cost, a, b))

# 간선 비용을 오름차순으로 정렬 (첫번째 원소인 cost 기준)
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost

print(res)
