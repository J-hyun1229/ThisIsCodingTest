# 회사 개수, 도로 개수
n, m = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 1 -> k -> x 차례로 방문
x, k = map(int, input().split())

for t in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][t] + graph[t][b])


res = graph[1][k] + graph[k][x]

if res >= INF:
    print(-1)
else:
    print(res)
