import time

start = time.perf_counter()
s = input()

sArr = []

for ch in s:
    sArr.append(int(ch))

# print(sArr) # test code

sArr.sort(reverse=True)

res = sArr[0]

for i in sArr[1:]:
    # 0은 곱하지 않고 더한다.
    if i == 0:
        continue
    if i == 1:
        res += 1
    res *= i

print(res)
end = time.perf_counter()

print("time: %.2fms" % (end-start))
