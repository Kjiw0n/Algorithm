from collections import deque

R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * C for _ in range(R)]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    wolf, sheep = 0, 0
    while queue:
        x, y = queue.popleft()
        if graph[y][x] == 'v':
            wolf += 1
        elif graph[y][x] == 'k':
            sheep += 1
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx] and graph[ny][nx] != '#':
                queue.append((nx, ny))
                visited[ny][nx] = True

    return wolf, sheep

wolf, sheep = 0, 0
for x in range(C):
    for y in range(R):
        if not visited[y][x]:
            w, s = bfs(x, y)
            if s > w:
                sheep += s
            else:
                wolf += w

print(sheep, wolf)
