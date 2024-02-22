from collections import deque

# (조건) 정점 번호가 작은 것을 먼저 방문
# (조건) 간선은 양방향

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

visited_dfs = [False] * (N + 1)
visited_bfs = [False] * (N + 1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in range(N + 1): # 어차피 이렇게 가면 graph[v]는 작은 노드부터 방문하게 됨
        if graph[v][i] == 1 and not visited_dfs[i]:
            dfs(i)

def bfs(v):
    queue = deque()
    visited_bfs[v] = True
    queue.append(v)
    while queue:
        dv = queue.popleft()
        print(dv, end=' ')
        for i in range(N + 1):
            if graph[dv][i] == 1 and not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(V)
print()
bfs(V)