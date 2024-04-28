N, M = map(int, input().split())

arr = []
visited = [False] * N

def backTracking(v):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(v, N):
        if not visited[i]:
            arr.append(i + 1)
            visited[i] = True
            backTracking(i)
            visited[i] = False
            arr.pop()

backTracking(0)