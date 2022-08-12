# find()에 경로 압축 기법을 적용하여 시간 복잡도를 개선한 코드
def find_parent(parent, node):
    if parent[node] != node:
        # 부모 테이블을 루트노드로 업데이트한다.
        parent[node] = find_parent(parent, parent[node])
    # 부모 노드가 자기자신이면 루트노드
    return parent[node]


def union_parent(parent, node1, node2):
    node1 = find_parent(parent, node1)
    node2 = find_parent(parent, node2)
    # 더 작은 쪽을 부모노드로 설정.
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2


# 노드 개수, 간선 개수(union 연산 개수)
v, e = map(int, input().split())
parent = [0] * (v+1)

# 자기 자신을 부모노드로 초기화.
for i in range(1, v+1):
    parent[i] = i

# 정해진 횟수만큼 union연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end= ' ')

print()

print("부모 테이블: ", end='')
for i in range(1, v+1):
    print(parent[i], end=' ')

