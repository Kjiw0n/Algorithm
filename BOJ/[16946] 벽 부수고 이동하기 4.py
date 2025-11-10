import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(N, M, graph, i, j, visited, dist):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    cells = [(i, j)]  # 이번 영역에 포함된 칸들 저장

    cnt = 1
    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                queue.append((ny, nx))
                cells.append((ny, nx))
                cnt += 1

    for (y, x) in cells:
        dist[y][x] = cnt

def res_cnt(N, M, graph, i, j, dist):
    adj = set()
    for d in range(4):
        ny = i + dy[d]
        nx = j + dx[d]
        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
            adj.add((ny, nx))
    total = 1
    for (y, x) in adj:
        total += dist[y][x]
    return total % 10


N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(N, M, graph, i, j, visited, dist)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            graph[i][j] = res_cnt(N, M, graph, i, j, dist)

for g in graph:
    print(''.join(map(str, g)))
