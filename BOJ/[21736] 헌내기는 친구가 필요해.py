from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = []
doyeon = 0
for i in range(N):
    g = list(input().strip())
    if 'I' in g:
        for j in range(M):
            if 'I' == g[j]:
                doyeon = (j, i)
    graph.append(g)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * M for _ in range(N)]
def bfs(x, y):
    global cnt
    cnt = 0
    queue = deque()
    visited[y][x] = True
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if graph[ny][nx] != 'X':
                    # 이동 가능
                    if graph[ny][nx] == 'P':
                        cnt += 1
                    visited[ny][nx] = True
                    queue.append((nx, ny))

bfs(doyeon[0], doyeon[1])
if cnt == 0:
    print('TT')
else:
    print(cnt)
