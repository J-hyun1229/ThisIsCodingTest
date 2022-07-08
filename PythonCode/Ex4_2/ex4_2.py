n = int(input())

count = 0

for i in range(n+1):
    timeStr = ''
    for j in range(60):
        for k in range(60):
            timeStr = str(i) + str(j) + str(k)
            if timeStr.find('3') != -1 :
                count += 1

print(count);

# 예시 답안과 같은 내용임