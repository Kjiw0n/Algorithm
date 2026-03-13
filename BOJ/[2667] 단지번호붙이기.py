from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

visited = [[False] * N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    cnt = 0
    while queue:
        tx, ty = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] != 0:
                queue.append((nx, ny))
                visited[ny][nx] = True

    return cnt

res = []
for y in range(N):
    for x in range(N):
        if not visited[y][x] and graph[y][x] != 0:
            res.append(bfs(x, y))

res.sort()
print(len(res))
for r in res:
    print(r)
