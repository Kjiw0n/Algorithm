N, M = map(int, input().split())

numArr = [i for i in range(1, N + 1)]

def dfs(arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        arr.append(numArr[i])
        dfs(arr)
        arr.pop()

dfs([])