import sys
from collections import deque

input = sys.stdin.readline

# 낮일때만 벽을 부술 수 있다.
# 밤일때는 벽을 부술 수 없다.
# 방문 칸 개수에 따라 낮, 밤 결정 (낮: 홀수, 밤: 짝수)


def bfs(N, M, K, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]

    queue = deque()
    queue.append((0, 0, 0, 1)) # y, x, b, dist
    visited[0][0][0] = True

    while queue:
        y, x, b, dist = queue.popleft()
        if (y, x) == (N - 1, M - 1):
            return dist

        isDay = dist % 2 == 1 # 낮: 홀수, 밤: 짝수

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0 and not visited[ny][nx][b]:
                    visited[ny][nx][b] = True
                    queue.append((ny, nx, b, dist + 1))
                elif graph[ny][nx] == 1 and b < K and not visited[ny][nx][b + 1]:
                    if isDay:
                        # 부실 수 있다.
                        visited[ny][nx][b + 1] = True
                        queue.append((ny, nx, b + 1, dist + 1))
                    else:
                        # 부실 수 없다. 제자리에서 기다려야함
                        queue.append((y, x, b, dist + 1)) # 본인 다시 넣기

    return -1

N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().strip())))

print(bfs(N, M, K, graph))