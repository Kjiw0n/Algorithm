import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def backTracking(v, r):
    if len(r) == M:
        # 다 본거임
        print(*r)
        return

    prev_n = -1
    for i in range(v, N):
        if prev_n != arr[i]:
            r.append(arr[i])
            backTracking(i, r)
            prev_n = arr[i]
            r.pop()

backTracking(0, [])
