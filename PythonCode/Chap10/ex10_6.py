from collections import deque

v, e = map(int, input().split())

# 진입 차수 리스트
in_degree = [0] * (v+1)

graph = [[] for i in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)  # 노드 a에서 b로 이동 가능
    in_degree[b] += 1


def topology_sort():
    result = []  # 정렬 결과를 저장할 리스트
    q = deque()

    # 첫 시행 시 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, v+1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:  # graph[now]: now 노드와 간선이 연결된 노드들
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()
