import sys

input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = 0
start = 0
end = arr[len(arr) - 1]
while start <= end:
    mid = (start + end) // 2
    total = 0
    for a in arr:
        if a > mid:
            total += a - mid
    if total < M:
        end = mid - 1
    else:
        ans = mid
        start = mid + 1

print(ans)
