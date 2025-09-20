from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
res = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            queue = deque()
            queue.append((j, i))
            visited[i][j] = True

            global x, y
            cnt = 0

            while queue:
                x, y = queue.popleft()
                cnt += 1
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and graph[ny][nx] == 1:
                        visited[ny][nx] = True
                        queue.append((nx, ny))

            res.append(cnt)

print(len(res))
if len(res):
    print(max(res))
else:
    print(0)