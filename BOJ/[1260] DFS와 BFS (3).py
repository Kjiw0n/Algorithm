from collections import deque
import sys

input = sys.stdin.readline

def dfs(graph, visited, v):
    visited[v] = True
    print(v + 1, end=' ')

    for i in range(N):
        if not visited[i] and graph[v][i]:
            dfs(graph, visited, i)

def bfs(graph, visited, v):
    queue = deque()
    visited[v] = True
    queue.append(v)
    print(v + 1, end=' ')

    while queue:
        q = queue.popleft()
        for i in range(N):
            if not visited[i] and graph[q][i]:
                visited[i] = True
                queue.append(i)
                print(i + 1, end=' ')

N, M, V = map(int, input().split())

graph = [[0] * N for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x - 1][y - 1] = 1
    graph[y - 1][x - 1] = 1

visited = [False] * N
dfs(graph, visited, V - 1)
print()
visited = [False] * N
bfs(graph, visited, V - 1)