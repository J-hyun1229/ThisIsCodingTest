import time

start = time.perf_counter()
s = input()

sArr = []

for ch in s:
    sArr.append(int(ch))

# print(sArr) # test code
res = sArr[0]

for i in sArr[1:]:
    if (res == 0) or (i<2):
        res += i
    else:
        res *= i

print(res)
end = time.perf_counter()

print("time: %.2fms" % (end-start))
