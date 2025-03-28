graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]

visited = [False] * 9

from collections import deque

queue = deque()
queue.append(1)
visited[1] = True

while queue:
    q = queue.popleft()
    print(q, end=' ')
    for i in graph[q]:
        if not visited[i]:
            queue.append(i)
            visited[i] = True
