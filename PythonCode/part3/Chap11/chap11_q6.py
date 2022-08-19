def solution(food_times, k):
    answer = 0
    length = len(food_times)
    ft = []

    if sum(food_times) <= k:
        return -1
    while k >= 0:
        print("k: %d,"%k, "food_times =", food_times)

        for i in range(0, length):
            if food_times[i] == 0:
                continue
            else:
                if k == 0:  # 방송이 중단된 시점에 먹어야할 음식의 인덱스는 i
                    answer = i + 1  # 음식 번호는 인덱스+1 이므로 answer에 i+1 저장.
                    k -= 1
                    break
                print("eat food[%d]"%i)
                food_times[i] -= 1
                k -= 1

    return answer


arr = [3, 1, 2]
n = 5

ans = solution(arr, n)
print(ans)
