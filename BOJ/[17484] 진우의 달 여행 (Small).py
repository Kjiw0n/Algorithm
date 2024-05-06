N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1]

result = 1000 # 원소 최댓값: 100

def solve(y, x, d):
    if y == N:
        return 0

    min_y = 1000
    for i in range(3):
        if i == d:
            # 이전에 움직인 방향
            continue

        nx = x + dx[i]
        if 0 <= nx < M:
            min_y = min(min_y, solve(y + 1, nx, i) + graph[y][x])

    return min_y

for i in range(M):
    result = min(result, solve(0, i, -1))

print(result)