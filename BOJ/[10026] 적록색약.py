from collections import deque

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[False] * N for _ in range(N)]
visited_blind = [[False] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
cnt_b = 0

def bfs(S, graph, visited, N, i, j):
    queue = deque()
    queue.append((j, i))
    visited[i][j] = True
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] in S:
                visited[ny][nx] = True
                queue.append((nx, ny))

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(graph[i][j], graph, visited, N, i, j)
            cnt += 1
        if not visited_blind[i][j]:
            if graph[i][j] == 'B':
                bfs(graph[i][j], graph, visited_blind, N, i, j)
            else:
                bfs(('R', 'G'), graph, visited_blind, N, i, j)
            cnt_b += 1

print(cnt, cnt_b)