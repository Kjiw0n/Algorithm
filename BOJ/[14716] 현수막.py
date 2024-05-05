import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = []
for _ in range(M):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

visited = [[False] * N for _ in range(M)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == 1:
                    queue.append((nx, ny))

cnt = 0
for x in range(N):
    for y in range(M):
        if not visited[y][x] and graph[y][x] == 1:
            bfs(x, y)
            cnt += 1

print(cnt)
