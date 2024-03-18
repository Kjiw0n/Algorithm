N = int(input())
arr = []
for i in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x:(x[1], x[0]))

count = 1
end_time = arr[0][1]
for i in range(1, N):
    if arr[i][0] >= end_time:
        count += 1
        end_time = arr[i][1]

print(count)