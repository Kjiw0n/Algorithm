# 얼음만들기랑 똑같네
# 상하좌우 확인하고
# 1 있으면 방문처리 하고 그 다음으로
# 0인 경우 -> return False
# -> dfs
# 인접되어있는 부분 끝날 때까지 (재귀 끝날 때까지) 반복하다가 result += 1
import sys

sys.setrecursionlimit(10000) # 파이썬은 재귀 깊이가 1000까지이므로(기본설정) 바꿔주기

T = int(input())

result = []
for t in range(T):
    M, N, K = map(int, input().split())

    # graph의 인덱스 0도 채움
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(i, j):
        if graph[i][j] == 1:
            graph[i][j] = 0
            for d in range(4):
                di = i + dx[d]
                dj = j + dy[d]
                if 0 <= di < N and 0 <= dj < M:
                    dfs(di, dj)
            return True
        else:
            return False

    count = 0
    for i in range(N):
        for j in range(M):
            if dfs(i, j):
                count += 1

    result.append(count)

print(*result, sep='\n')
