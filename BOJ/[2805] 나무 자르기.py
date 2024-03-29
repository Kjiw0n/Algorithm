import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while start <= end:
    mid = (start + end) // 2

    total = 0
    for a in arr:
        if a > mid:
            total += a - mid

    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)