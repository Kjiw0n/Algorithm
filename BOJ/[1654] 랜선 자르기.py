import sys

input = sys.stdin.readline

K, N = map(int, input().split())

arr = []
for _ in range(K):
    arr.append(int(input()))

start = 1
end = max(arr)

result = min(arr)
while start <= end:
    mid = (start + end) // 2
    count = 0
    for a in arr:
        count += a // mid

    if count >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)