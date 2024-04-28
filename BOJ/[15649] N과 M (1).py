N, M = map(int, input().split())

arr = []
visited = [False] * N
def backTracking():
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        if not visited[i]:
            arr.append(i + 1)
            visited[i] = True
            backTracking()
            visited[i] = False
            arr.pop()


backTracking()

