from collections import deque
import sys

input = sys.stdin.readline

M, N, H = map(int, input().split())

graph = []
apples = []
for z in range(H):
    gg = []
    for y in range(N):
        g = list(map(int, input().split()))
        for x in range(M):
            if g[x] == 1:
                apples.append((x, y, z))
        gg.append(g)
    graph.append(gg)

# print(graph)
# print(apples)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(cnt = -1):
    queue = deque(apples)
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            # print('cnt: ', cnt, 'x, y, z: ', x, y, z)

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = 1
                    queue.append((nx, ny, nz))
    return cnt

result = bfs()

for z in range(H):
    for y in range(N):
        for x in range(M):
            if graph[z][y][x] == 0:
                result = -1

print(result)
