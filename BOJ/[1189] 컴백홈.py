import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

R, C, K = map(int, input().split())

graph = []
for i in range(R):
    graph.append(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * C for _ in range(R)]

def backTracking(x, y, visited, count):
    if x == C - 1 and y == 0:
        # print('count: ', count)
        if count == K:
            global result
            result += 1
        return

    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and not visited[ny][nx]:
            if graph[ny][nx] != 'T':
                backTracking(nx, ny, visited, count + 1)
            visited[ny][nx] = False

result = 0
backTracking(0, R - 1, visited, 1)

print(result)
