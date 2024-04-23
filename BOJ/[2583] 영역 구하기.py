from collections import deque
import sys

input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[1] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            graph[y][x] = 0

# for g in graph:
#     print(*g)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    x, y = 0, 0
    a = 0
    while queue:
        x, y = queue.popleft()
        # print('x, y: ', x, y, 'graph[y][x]: ', graph[y][x])
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                a += 1
                queue.append((nx, ny))

    return a # 방문한 노드 개수

count = 0
area = []
for x in range(N):
    for y in range(M):
        if graph[y][x] == 1:
            count += 1
            a = bfs(x, y)
            if a == 0:
                area.append(1)
            else:
                area.append(a)

area.sort()
print(count)
print(*area)