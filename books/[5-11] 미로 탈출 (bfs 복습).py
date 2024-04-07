from collections import deque

N, M, = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
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


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[N - 1][M - 1]

print(bfs(0, 0))
