from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for d in range(len(dx)):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs(graph, 0, 0)
print(graph[N - 1][M - 1])
