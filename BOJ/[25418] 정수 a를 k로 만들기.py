from collections import deque

n, k = map(int, input().split())

visited = [False] * (k + 1)

cnt = [0] * (k + 1)

queue = deque()
queue.append(n)
visited[n] = True

while queue:
    x = queue.popleft()

    if x >= k:
        print(cnt[x])
        exit()

    for i in range(2):
        x1 = x + 1
        x2 = x * 2
        if x1 <= k and not visited[x1]:
            queue.append(x1)
            visited[x1] = True
            cnt[x1] = cnt[x] + 1
        if x2 <= k and not visited[x2]:
            visited[x2] = True
            queue.append(x2)
            cnt[x2] = cnt[x] + 1
