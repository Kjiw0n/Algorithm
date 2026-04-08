# 오름차순을 유지하는 길이가 M인 수열

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]

def dfs(prev, arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(prev, N):
        arr.append(nums[i])
        dfs(i, arr)
        arr.pop()

dfs(0, [])
