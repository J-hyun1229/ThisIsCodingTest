# ex3-1 (Greedy Algorithm)


money = int(input("거슬러줘야할 액수 입력>> "))

# 동전 종류
coin_k = [500, 100, 50, 10]

# 500, 100, 50, 10원 동전 개수
coins = [0,0,0,0]

total = 0

for i in range(0, 4):
    coins[i] = money // coin_k[i]
    money %= coin_k[i]
    total += coins[i]

print("거슬러줘야 할 동전의 최소 개수: %d" % total)



# 문제 정답

money = int(input("거슬러줘야할 액수 입력>> "))

coin = [500, 100, 50, 10]
res = 0

for i in coin:
    res += money // i
    money %= i

print("거슬러줘야 할 동전의 최소 개수: %d" % res)
