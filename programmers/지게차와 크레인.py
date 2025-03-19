from collections import deque


# 뺀 건 ' ', 이번 텀에 뺀 건 'b',
def bfs(graph, v, qx, qy, dx, dy, n, m):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((qx, qy))
    visited[qx][qy] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == v:
                    graph[nx][ny] = 'b'
                if graph[nx][ny] == ' ':
                    queue.append((nx, ny))
                visited[nx][ny] = True


def bToa(graph):
    for i, gr in enumerate(graph):
        for j, g in enumerate(gr):
            if g == 'b':
                graph[i][j] = ' '


def solution(storage, requests):
    graph = [list(' ' * (len(storage[0]) + 2))]
    for s in storage:
        g = [' ']
        for ss in s:
            g.append(ss)
        g.append(' ')
        graph.append(g)
    graph.append(list(' ' * (len(storage[0]) + 2)))

    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    n = len(graph)
    m = len(graph[0])
    print(n, m)

    for r in requests:
        if len(r) == 1:
            bfs(graph, r, 0, 0, dx, dy, n, m)
            bfs(graph, r, n - 1, 0, dx, dy, n, m)
            bfs(graph, r, 0, m - 1, dx, dy, n, m)
            bfs(graph, r, n - 1, m - 1, dx, dy, n, m)
            bToa(graph)
        else:
            for i, gr in enumerate(graph):
                for j, g in enumerate(gr):
                    if g == r[0]:
                        graph[i][j] = ' '

    cnt = 0
    for gr in graph:
        for g in gr:
            if g != ' ':
                cnt += 1
    return cnt