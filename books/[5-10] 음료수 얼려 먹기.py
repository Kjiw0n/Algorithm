# s 17:00 (30분)
# e 17:20 (- 10분 x)

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(i, j):
    if graph[i][j] == 0:
        graph[i][j] = 1
        for d in range(4): 
            di = i + dx[d]
            dj = j + dy[d]
            if 0 <= di < N and 0 <= dj < M:
                dfs(di, dj) # 방문 처리만
        return True
    else:
        return False

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)
