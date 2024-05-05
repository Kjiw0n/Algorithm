from collections import deque
import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)
result = [-1] * (N + 1)

def bfs(v, result):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        q = queue.popleft()
        # print(q, 'result: ', result[q])
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                result[i] = result[q] + 1

result[R] = 0
bfs(R, result)

for i in range(1, N + 1):
    print(result[i])
