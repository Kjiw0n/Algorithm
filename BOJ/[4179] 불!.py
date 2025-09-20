from collections import deque

R, C = map(int, input().split())
graph = []
fire_time = [[-1] * C for _ in range(R)]
j_time = [[-1] * C for  _ in range(R)]

queue = deque()
queue_fire = deque()
for i in range(R):
    g = list(input())
    for j in range(C):
        if g[j] == 'J':
            queue.append((j, i))
            j_time[i][j] = 0
        if g[j] == 'F':
            queue_fire.append((j, i))
            fire_time[i][j] = 0
    graph.append(g)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue_fire:
    x, y = queue_fire.popleft()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < C and 0 <= ny < R:
            if graph[ny][nx] != '#' and fire_time[ny][nx] == -1:
                fire_time[ny][nx] = fire_time[y][x] + 1
                queue_fire.append((nx, ny))

while queue:
    x, y = queue.popleft()
    if x in (0, C-1) or y in (0, R-1):
        print(j_time[y][x] + 1)
        exit()
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < C and 0 <= ny < R:
            if graph[ny][nx] != '#' and j_time[ny][nx] == -1:
                if fire_time[ny][nx] == -1 or j_time[y][x] + 1 < fire_time[ny][nx]:
                    j_time[ny][nx] = j_time[y][x] + 1
                    queue.append((nx, ny))

print("IMPOSSIBLE")
