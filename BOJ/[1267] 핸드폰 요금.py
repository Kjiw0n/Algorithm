# 핸드폰 요금은 (몫+1) * 요금 만큼 계산됨
# 영식: ((초 // 30) + 1) * 10
# 민식: ((초 // 60) + 1) * 15

n = int(input())
call_time = list(map(int, input().split()))

price_y = 0
price_m = 0
for i in range(n):
    price_y += ((call_time[i] // 30) + 1) * 10
    price_m += ((call_time[i] // 60) + 1) * 15

if price_y > price_m:
    print('M', price_m)
elif price_y == price_m:
    print('Y M', price_y)
else:
    print('Y', price_y)
