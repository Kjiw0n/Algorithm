N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(str, input().split())))

arr.sort(key=lambda x: x[1])

for a in arr:
    print(a[0], end=' ')
