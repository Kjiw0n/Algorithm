from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

visited = [[False] * M for _ in range(N)]
cnt = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, vx, vy, visited):
    # print('start', vx, vy)
    queue = deque([])
    queue.append((vx, vy))
    visited[vx][vy] = True
    while queue:
        x, y = queue.popleft()
        # print('x, y', x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print('x, y', x, y, 'nx ny:', nx, ny, 'd', dx, dy)
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == '0':
                queue.append((nx, ny))
                visited[nx][ny] = True
    return

for x in range(N):
    for y in range(M):
        if not visited[x][y] and graph[x][y] != '1':
            bfs(graph, x, y, visited)
            cnt += 1

print(cnt)


