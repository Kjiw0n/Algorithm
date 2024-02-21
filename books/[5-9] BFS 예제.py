from collections import deque

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visit = [False] * 9

def bfs(graph, i, visit):
    queue = deque([i])

    visit[i] = True

    while queue: # 큐가 빌 때까지 반복
        v = queue.popleft()
        print(v, end = ' ')

        for j in graph[v]:
            if not visit[j]:
                queue.append(j)
                visit[j] = True

bfs(graph, 1, visit)