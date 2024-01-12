K, N, M = map(int, input().split())
tot_price = K * N
now = tot_price - M

if now > 0:
    print(now)
else:
    print(0)