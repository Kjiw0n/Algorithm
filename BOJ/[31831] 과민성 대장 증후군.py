N, M = map(int, input().split())

arr = list(map(int, input().split()))

cnt = 0
result = 0
for a in arr:
    if cnt + a >= 0:
        cnt += a
    else:
        cnt = 0
    if cnt >= M:
        result += 1

print(result)
