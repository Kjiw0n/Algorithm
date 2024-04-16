from collections import deque

graph = []
for i in range(5):
    graph.append(list(map(int, input().split())))

r, c = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * 5 for _ in range(5)]
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    graph[x][y] = 1
    x, y = 0, 0
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    return (x, y)
                elif graph[nx][ny] == -1:
                    continue
                queue.append((nx, ny))
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
        # print(queue)
    return -1, -1

x, y = bfs(r, c)
# for g in graph:
#     print(*g)
#
# print((x, y))
if x < 0:
    print(-1)
else:
    print(graph[x][y])
