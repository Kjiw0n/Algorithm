import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

if sum(arr) <= M:
    print(max(arr))
else:
    s = 0
    e = max(arr)
    result = 0
    while s <= e:
        m = (s + e) // 2

        total = 0
        for a in arr:
            total += min(a, m)
        if total <= M:
            result = m
            s = m + 1
        else:
            e = m - 1

    print(result)
