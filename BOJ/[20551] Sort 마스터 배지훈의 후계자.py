from bisect import bisect_left
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arrA = []
for _ in range(N):
    arrA.append(int(input()))

arrB = sorted(arrA)

for _ in range(M):
    d = int(input())
    i = bisect_left(arrB, d)
    # if d in arrB: -> 시간초과 남
    if i < N and arrB[i] == d:
        print(i)
    else:
        print(-1)
