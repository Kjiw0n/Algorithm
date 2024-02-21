# s 21:18 (30분)
# e 22:17 (+ 60 x)

from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 인접한 노드 중에 1이 있냐 -> 상하좌우로 움직임
# 목적지와 가장 가까운 1로 이동
# 최단거리 -> BFS

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y)) # 방문처리
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            # 상하좌우 인접한 노드 중 1이 있는 지 확인 -> 있다면 해당 노드 값 = 최상단노드 값 + 1
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                # 범위 만족 시
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1  # 방문처리
                    queue.append((nx, ny))
    return graph[N - 1][M - 1]

print(bfs(0, 0))