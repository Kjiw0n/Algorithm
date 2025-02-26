N, M = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False] * M for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 4방향 다 실패 시 -> 멈춤
cnt = 1 # 방문한 칸 개수
dnt = 1 # 방문한 방향 개수
while True:
    visited[x][y] = True
    d += 1
    if d >= 4:
        d = 0
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1 and not visited[nx][ny]:
        x, y = nx, ny
        cnt += 1
        dnt = 1
        continue
    dnt += 1
    # 후진
    if dnt >= 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                break
            x, y = nx, ny
            dnt = 1
            continue

print(cnt)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1