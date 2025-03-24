# 17:13

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
max_c = 0
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    max_c = max(max_c, c)

A, B = map(int, input().split())
s = 1
e = max_c
ans = 0

while s <= e:
    mid = (s + e) // 2
    visited = [False] * (N + 1)
    queue = deque()
    queue.append(A)
    visited[A] = True
    flag = False

    while queue:
        q = queue.popleft()
        if q == B:
            flag = True
            break
        for nq, c in graph[q]:
            if not visited[nq] and c >= mid:
                visited[nq] = True
                queue.append(nq)
    if flag:
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)