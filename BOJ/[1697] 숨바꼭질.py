from collections import deque

N, K = map(int, input().split())

visited = [False] * 100001
def bfs(N, K):
    queue = deque()
    queue.append((N, 0))
    visited[N] = True
    while queue:
        q, t = queue.popleft()
        if q == K:
            return t
        for nq in (q - 1, q + 1, q * 2):
            if 0 <= nq <= 100000 and not visited[nq]:
                visited[nq] = True
                queue.append((nq, t + 1))

print(bfs(N, K))
