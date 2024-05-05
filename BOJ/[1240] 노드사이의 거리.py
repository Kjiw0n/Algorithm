import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
for i in range(N - 1):
    x, y, w = map(int, input().split())
    arr[x].append([y, w])
    arr[y].append([x, w])

def bfs(s, e):
    queue = deque()
    queue.append((s, 0))
    visited[s] = True

    while queue:
        q, d = queue.popleft()
        if q == e:
            return d
        for a, w in arr[q]:
            if not visited[a]:
                visited[a] = True
                queue.append((a, d + w))



for _ in range(M):
    x, y = map(int, input().split())
    visited = [False] * (N + 1)
    print(bfs(x, y))
