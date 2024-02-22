from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

# print(graph)

# 어차피 무조건 (1, 1) 에서부터 시작. 끝은 (N, M)
# 최단거리 -> bfs

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    while queue:
        # print(queue)
        x, y = queue.popleft()
        for d in range(4):
            di = x + dx[d]
            dj = y + dy[d]
            if 0 <= di < N and 0 <= dj < M:
                if graph[di][dj] == 1:
                    graph[di][dj] = graph[x][y] + 1
                    queue.append((di, dj))
                    # print('di, dj: ', di, dj, 'graph[', di, '][', dj, ']: ', graph[di][dj] + 1)
    print(graph[N - 1][M - 1])

bfs(0, 0)