from collections import deque

N, M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(input()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0, 0)) # y, x, brokeFlag
    visited[0][0][0] = 1 # 방문 노드 개수 카운팅

    while queue:
        y, x, b = queue.popleft()
        if (y, x) == (N - 1, M - 1):
            return visited[y][x][b]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == '0' and visited[ny][nx][b] == 0:
                    # 0이면, visited 안한 경우 방문 가능
                    visited[ny][nx][b] = visited[y][x][b] + 1
                    queue.append((ny, nx, b))
                elif graph[ny][nx] == '1' and b == 0:
                    # 1이면, 벽 부수지 않은 경우에 한해 방문 가능
                    visited[ny][nx][1] = visited[y][x][b] + 1
                    queue.append((ny, nx, 1)) 

    return -1

print(bfs(graph))