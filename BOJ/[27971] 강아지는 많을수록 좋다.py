from collections import deque

N, M, A, B = map(int, input().split())

num = [A, B]

arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))

visited = [False] * (N + 1)
def bfs(v = 0, cnt = 0):
    queue = deque()
    queue.append((v, cnt))
    visited[v] = True
    while queue:
        q, cnt = queue.popleft()
        if q == N:
            return cnt
        for n in num:
            flag = True
            for m in arr:
                if m[0] <= q + n <= m[1]:
                    flag = False
            if flag and q + n <= N and not visited[q + n]:
                queue.append((q + n, cnt + 1))
                visited[q + n] = True
    return -1

print(bfs())
