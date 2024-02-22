# bfs로 전파됨

# N 노드 개수
# M 간선 개수
# 번호 쌍 주어짐
from collections import deque

N = int(input())
M = int(input())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

visited = [False] * (N + 1)

def bfs(v, count):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        v = queue.popleft()
        for i in range(N + 1):
            if graph[v][i] == 1 and not visited[i]:
                # 연결은 되어있는데 방문처리가 안되어있다면
                queue.append(i)
                count += 1
                visited[i] = True
    print(count)

bfs(1, 0) # '1번 컴퓨터를 통해 바이러스에 걸리는 컴퓨터의 수'를 출력하는 거니까 1번 컴퓨터는 카운트 x