from collections import deque
import sys

input = sys.stdin.readline

# 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다.
# 왼쪽, 오른쪽, 앞, 뒤 네 방향
# 토마토가 혼자 저절로 익는 경우는 없다고 가정
# -> 며칠이 지나면 다 익게 되는지, 그 최소 일수
#
# 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸



# -----
M, N = map(int, input().split())

graph = []
apple = []
# 익은 토마토가 어디에 있는 지 찾아야함!
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(M):
        if graph[i][j] == 1:
            apple.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(apple):
    queue = deque(apple)
    x, y = 0, 0
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return (x, y)

def check(graph):
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                return False
    return True

x, y = bfs(apple)
if check(graph):
    print(graph[x][y] - 1)
else:
    print(-1)
