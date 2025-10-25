from collections import deque

# 먼저 불 지르고, 각 초 별로 불난 위치랑 비교
# 처음 불 난 곳을 0, 그 다음부터 +1로 그래프 채우기

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def fired_bfs(w, h, graph, fires):
    fire_time = [[float('inf')] * w for _ in range(h)]
    queue = deque()
    for fy, fx in fires:
        queue.append((fy, fx))
        fire_time[fy][fx] = 0

    while queue:
        y, x = queue.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= nx < w and 0 <= ny < h:
                if graph[ny][nx] != '#' and fire_time[ny][nx] == float('inf'):
                    fire_time[ny][nx] = fire_time[y][x] + 1
                    queue.append((ny, nx))

    return fire_time


def bfs(w, h, graph, start, end, fire_time):
    visited = [[False] * w for _ in range(h)]
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True

    while queue:
        y, x, t = queue.popleft()
        if (y, x) in end:
            return t + 1
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and graph[ny][nx] != '#':
                if fire_time[ny][nx] > t + 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx, t + 1))

    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    w, h = map(int, input().split())
    graph = []
    start = (0, 0) # y, x
    end = [] # (y, x)
    fires = [] # (y, x)
    for i in range(h):
        g = list(input())
        for j in range(w):
            if g[j] == '@':
                start = (i, j)
            elif g[j] == '*':
                fires.append((i, j))
            if (i == 0 or i == h - 1 or j == 0 or j == w - 1) and g[j] in ('.', '@'):
                # 탈출 가능 위치
                end.append((i, j))
        graph.append(g)

    if end:
        fire_time = fired_bfs(w, h, graph, fires)
        print(bfs(w, h, graph, start, end, fire_time))
    else:
        print('IMPOSSIBLE')