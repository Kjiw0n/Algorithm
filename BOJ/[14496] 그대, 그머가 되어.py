from collections import deque

a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[0] * N for i in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

visited = [False] * N
def bfs(a, b):
    queue = deque()
    queue.append((a, 0))
    visited[a] = True

    while queue:
        q, count = queue.popleft()
        if q == b:
            return count

        for i in range(N):
            if not visited[i] and graph[q][i] == 1:
                queue.append((i, count + 1))
                visited[i] = True
    return -1

print(bfs(a - 1, b - 1))
