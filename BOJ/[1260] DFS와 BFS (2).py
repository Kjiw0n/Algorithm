from collections import deque
import sys

input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v + 1, end=' ')

    for i in range(N):
        if graph[v][i] == 1 and not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    queue = deque()
    queue.append(v)
    visited[v] = True
    print(v + 1, end=' ')
    while queue:
        d = queue.popleft()
        for i in range(N):
            if graph[d][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
                print(i + 1, end=' ')

N, M, V = map(int, input().split())

graph = [[0] * N for _ in range(N)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

visited = [False] * N
dfs(graph, V - 1, visited)
print()
visited = [False] * N
bfs(graph, V - 1, visited)
