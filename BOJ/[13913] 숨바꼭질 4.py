# 1. 가장 빠르게 도달하는 시간 구하기 (dist)
# 2. 가장 빠르게 찾는 이동 기록 구하기 (parent(dict)에 기록 저장)
# 2-2. 최단 이동 방법이 여러가지 인 경우 아무거나 출력하면 된다.
from collections import deque

N, K = map(int, input().split())
dist = [-1] * 100001
parent = {}

def bfs(N, K):
    queue = deque()
    queue.append(N)
    dist[N] = 0
    parent[N] = -1 # 맨 처음
    while queue:
        q = queue.popleft()
        if q == K:
            return
        for nq in (q - 1, q + 1, q * 2):
            if 0 <= nq < 100001:
                if dist[nq] == -1:
                    dist[nq] = dist[q] + 1
                    parent[nq] = q
                    queue.append(nq)

bfs(N, K)
print(dist[K])

res = [K]
idx = K
while parent[idx] != -1:
    idx = parent[idx]
    res.append(idx)

res.reverse()
print(*res)