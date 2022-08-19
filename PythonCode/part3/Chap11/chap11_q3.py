import time
start = time.perf_counter()

s = input()

p = s[0]

res = 1
change_count = 0

for ch in s[1:]:
    # print("cur ch: %c, p: %c" % (ch, p))
    if p != ch:
        change_count += 1
        # print("count added: cur count =", change_count)
        if change_count == 2:
            res += 1
            # print("res added: cur res = ", res)
            change_count = 0
        p = ch

if s[0] == s[-1]:
    print(res-1)
else:
    print(res)

end = time.perf_counter()

print("time: %.2fms" % (end-start))
