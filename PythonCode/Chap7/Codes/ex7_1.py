# 순차 탐색 알고리즘

def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1  # 인덱스에 1 더하여 위치 반환.


print("생성할 원소 개수 입력 후 한 칸 띄고 찾을 문자열 입력")

data = input().split()

n = int(data[0])
target = data[1]

print("원소 개수만큼 문자열 입력")

arr = input().split()

print(sequential_search(n, target, arr))
