import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * M for _ in range(N)]

def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = True

    while queue:
        x, y, cnt = queue.popleft()
        if x == M - 1 and y == N - 1:
            print(cnt)
            return
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                visited[ny][nx] = True
                if graph[ny][nx] == 0:
                    queue.appendleft((nx, ny, cnt))
                elif graph[ny][nx] == 1:
                    queue.append((nx, ny, cnt + 1))

bfs()