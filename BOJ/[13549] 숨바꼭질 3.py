from collections import deque

N, K = map(int, input().split())
dist = [-1] * 100001

def bfs(N):
    queue = deque()
    queue.append(N)
    dist[N] = 0
    while queue:
        q = queue.popleft()
        for nq in (q - 1, q + 1, q * 2):
            if 0 <= nq < 100001:
                if nq == q * 2:
                    cost = 0
                else:
                    cost = 1

                if dist[nq] == -1 or dist[nq] > dist[q] + cost:
                    dist[nq] = dist[q] + cost

                    if cost == 0:
                        queue.appendleft(nq)
                    else:
                        queue.append(nq)

bfs(N)
print(dist[K])
