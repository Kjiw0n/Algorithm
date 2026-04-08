N, M = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, max(arr)
h = 0

while s <= e:
    mid = (s + e) // 2
    total = 0
    for a in arr:
        if a > mid:
            total += (a - mid)

    if total >= M:
        s = mid + 1
        h = mid
    else:
        e = mid - 1

print(h)