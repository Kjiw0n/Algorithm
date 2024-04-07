from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

visited = [False] * N
def bfs(v):
    queue = deque()
    visited[v] = True
    queue.append(v)

    while queue:
        q = queue.popleft()
        for i in range(N):
            if graph[q][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

count = 0
for i in range(N):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)

