from collections import deque

n = int(input())

lec_time = [0] * (n+1)  # 강의 시간
pre_lec = [0] * (n+1)  # 선수 강의 개수 (진입 차수)
pre_time = [0] * (n+1)  # 선수강의를 듣는데 걸리는 시간

curr = [[] for i in range(n+1)]  # 커리큘럼 (graph)

for i in range(1, n+1):  # i: 강의 번호.
    data = list(map(int, input().split()))  # i번 강의에 대한 정보 입력받음
    lec_time[i] = data[0]

    for j in data[1:]:
        if j == -1:
            break
        curr[j].append(i)  # i의 선수강의가 j (j->i). data[j]는 i의 선수강의들.
        pre_lec[i] += 1  # 진입차수


def topology_sort():
    # sort_res = []
    q = deque()

    # 처음 실행 시 진입 차수가 0인 노드들을 큐에 삽입.
    for i in range(1, n+1):
        if pre_lec[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()  # 진입차수가 0인 노드를 꺼낸다.
        # sort_res.append(now)
        for i in curr[now]:  # curr[now]에는 now와 연결된 노드들이 들어있음.
            pre_lec[i] -= 1  # 간선 제거 (진입차수 -1)

            # 저장된 선수 강의 시간이 now의 시간(now의 선수강의 포함)보다 작으면 now의 시간으로 변경.
            if pre_time[i] < pre_time[now] + lec_time[now]:
                pre_time[i] = pre_time[now] + lec_time[now]

            if pre_lec[i] == 0:
                q.append(i)


topology_sort()

for i in lec_time:
    print(i, end=' ')

print()

for i in pre_time:
    print(i, end=' ')
print()

print("=====res====")
for i in range(1, n+1):
    print(pre_time[i] + lec_time[i])
