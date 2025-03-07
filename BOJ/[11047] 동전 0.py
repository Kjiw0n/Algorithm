N, K = map(int, input().split())

arr = []
for _ in range(N):
    a = int(input())
    if a > K:
        continue
    arr.append(a)

arr.reverse()

cnt = 0
for a in arr:
    cnt += K // a
    K %= a

print(cnt)