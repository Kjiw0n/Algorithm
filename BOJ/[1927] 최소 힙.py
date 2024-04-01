import sys
import heapq

input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    n = int(input())
    if n == 0:
        if pq:
            print(heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, n)

