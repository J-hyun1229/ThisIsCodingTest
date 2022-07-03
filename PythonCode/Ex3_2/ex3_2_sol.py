# 교재의 답안을 참고하여 개선한 코드

# n:배열 길이, m:더할 횟수, k:제한 반복 횟수
n, m, k = map(int, input().split())

data = list( map(int, input().split()) )

data.sort()
data.reverse()

first = data[0]
second = data[1]

res = 0
count = 0

for i in range(0, m) :
    if count == 3 :
        res += second
        count = 0
    else :
        res += first
        count += 1

print(res)


# 반복되는 수열을 이용한 풀이

res2 = 0
count2 = m // (k+1) * k
count2 += m % (k+1)

res2 += count2 * first
res2 += (m-count2) * second

print(res2)
