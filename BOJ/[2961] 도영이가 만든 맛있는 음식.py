import sys

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def backTracking(x, y, visited):
    global result
    if sum(visited) != 0:
        result = min(result, abs(x - y))
    # print(x, y)
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            backTracking(x * arr[i][0], y + arr[i][1], visited)
            visited[i] = False

result = 1e9
visited = [False] * N
backTracking(1, 0, visited)
print(result)
