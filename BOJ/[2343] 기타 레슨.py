import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = sum(arr)

result = 0
while start <= end:
    mid = (start + end) // 2

    count = 1
    m = mid
    for a in arr:
        if mid < a:
            count = M + 1
            break
        m -= a
        if m < 0:
            count += 1
            m = mid - a

    if count <= M:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)


