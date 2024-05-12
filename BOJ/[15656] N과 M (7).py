import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

def backTracking(v, r):
    if len(r) == M:
        print(*r)
        return

    for a in arr:
        r.append(a)
        backTracking(v, r)
        r.pop()

backTracking(0, [])
