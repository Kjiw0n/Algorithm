import sys
from collections import deque

input = sys.stdin.readline

def bfs(N, M, K, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        y, x, b = queue.popleft()
        if (y, x) == (N - 1, M - 1):
            return visited[y][x][b]
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < M and 0 <= ny < N:
                # 벽인데 벽 부실 횟수가 남아있는 경우
                if graph[ny][nx] == '1' and b < K and visited[ny][nx][b + 1] == 0:
                    visited[ny][nx][b + 1] = visited[y][x][b] + 1
                    queue.append((ny, nx, b + 1))
                # 벽 아님 (방문 여부 확인 후 걍 가면 됨)
                elif graph[ny][nx] == '0' and visited[ny][nx][b] == 0:
                    visited[ny][nx][b] = visited[y][x][b] + 1
                    queue.append((ny, nx, b))

    return -1

N, M, K = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(input().strip()))

print(bfs(N, M, K, graph))

