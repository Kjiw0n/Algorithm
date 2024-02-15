# 00시 00분 00초 ~ N시 59분 59초

N = int(input())

# 총 경우의 수: 24*60*60 = 86400
# => 10만개도 안됨. 그냥 하나하나 세도 2초 내에 충분히 해결 가능

count = 0
for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            # if h, m, s 중 하나가 3을 포함:
            if (str(h)+str(m)+str(s)).count('3') != 0:
                count += 1

print(count)