import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())

graph = []
for i in range(N):
    g = list(map(int, input().split()))
    for j in range(M):
        if g[j] == 2:
            gram = (j, i)
    graph.append(g)

# for g in graph:
#     print(*g)
#
# print(gram)

# 그람을 찾는 경우가 무조건 빠른가?
# 맞다면, 무조건 그람 찾고 직진하면 됨
# 아니라면? 그람 찾고 직진 루트, 냅다 공주한테 가는 루트 둘 다 해보고 비교해봐야함 -> 작아서 할 수 있긴 함. 모르겠으니까 걍 비교하자

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs():
    global cnt
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0, cnt))
    visited[0][0] = True
    while queue:
        x, y, cnt = queue.popleft()
        if x == M - 1 and y == N - 1:
            # print('cnt: ', cnt)
            return cnt
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if graph[ny][nx] == 0:
                    queue.append((nx, ny, cnt + 1))
                    visited[ny][nx] = True

    return T + 1

cnt1 = bfs()

def bfs2():
    global cnt
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append((0, 0, cnt))
    visited[0][0] = True
    while queue:
        x, y, cnt = queue.popleft()
        if x == gram[0] and y == gram[1]:
            # print('그람 찾음 여기서부터 시작하면 됨')
            # 공주님 거리 수직계산하면 끝
            cnt += (M-1) - x
            cnt += (N-1) - y
            # print('cnt: ', cnt)
            return cnt
        # if x == M - 1 and y == N - 1:
        #     print('cnt: ', cnt)
        #     return
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
                if graph[ny][nx] != 1:
                    queue.append((nx, ny, cnt + 1))
                    visited[ny][nx] = True

    return T + 1


cnt2 = bfs2()

result = min(cnt1, cnt2)
if result <= T:
    print(result)
else:
    print('Fail')