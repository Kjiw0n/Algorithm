import sys

input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = 2
        cnt += 1

    turn = 0
    while turn < 4:
        d += 3
        d %= 4
        nx = r + dx[d]
        ny = c + dy[d]

        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            cnt += 1
            r, c = nx, ny
            break
        turn += 1

    if turn == 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 1:
            r, c = nx, ny
        else:
            print(cnt)
            break
