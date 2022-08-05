import heapq

INF = int(1e9)

# 도시 개수, 통로 개수, 메시지 발신지
n, m, c = map(int, input().split())

graph = [[] * i for i in range(n+1)]

# 시작 도시부터 해당 노드로 가는 최단 거리 리스트
distance = [INF] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))  # 노드 x와 연결된 노드 y와 간선 길이 z


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[c] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:  # i == (node, dist)
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

cityCount = 0
timeCount = 0

for i in range(1, n+1):
    if distance[i] != INF:
        cityCount += 1
        if not graph[i]:
            timeCount = max(timeCount, distance[i])

# 자기 자신 제외
cityCount -= 1

print(cityCount, timeCount)

