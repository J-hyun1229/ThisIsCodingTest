import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # 먹을 음식을 저장할 큐
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))  # 큐에 (시간, 번호)의 튜플로 저장.

    sum_val = 0  # 지금까지 먹는데 걸린 시간
    previous = 0  # 이전 음식을 다먹는데 걸리는 시간 (전에꺼 먹느라 테이블을 돌린 바퀴 수)
    length = len(food_times)

    # 지금까지 먹은 시간 + (현재 음식시간 - 이전 음식시간) * 음식 개수
    while sum_val + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]  # 현재 음식을 먹는데 걸리는 시간
        sum_val += (now-previous) * length
        length -= 1  # 한가지 음식을 다 먹었으므로 음식개수 1 감소.
        previous = now  # 다음 음식으로 넘어가기 전에 현재 음식 시간을 이전 음식시간에 저장.

    result = sorted(q, key=lambda x:x[1])

    return result[(k - sum_val) % length][1]
