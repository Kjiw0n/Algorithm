from collections import deque

def bfs(n, computers, visited, i):
    queue = deque()
    queue.append(i)
    visited[i] = True
    while queue:
        c = queue.popleft()
        for j in range(n):
            if not visited[j] and computers[c][j] == 1:
                visited[j] = True
                queue.append(j)

def solution(n, computers):
    visited = [False] * n
    cnt = 0
    for i in range(n):
        if not visited[i]:
            bfs(n, computers, visited, i)
            cnt += 1

    return cnt