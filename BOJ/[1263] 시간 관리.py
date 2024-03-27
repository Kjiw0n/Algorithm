N = int(input())

arr = []
for _ in range(N):
    t, s = map(int, input().split())
    arr.append([t, s])

arr.sort(key=lambda x: x[1], reverse=True)
# print(arr)

now = arr[0][1] - arr[0][0]
for i in range(1, N):
    if now < 0:
        now = -1
        break

    if now <= arr[i][1]:
        now -= arr[i][0]
    else:
        now = arr[i][1] - arr[i][0]

if now < 0:
    print(-1)
else:
    print(now)
