from collections import deque

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0

queue = deque([])
queue.append((0, 0))
while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
            # graph 방문 시 값 없데이트 하므로 visited 필요x -> 삭제
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

print(graph[N-1][M-1])