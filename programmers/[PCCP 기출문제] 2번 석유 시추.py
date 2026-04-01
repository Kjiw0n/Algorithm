# Todo: 시추관을 수직으로 단 한번만 뚫을 때, 가장 많은 석유 뽑는 위치 찾기

# 1. 각 노드별로 조회해서, 연결된 석유덩어리의 사이즈 및 포함된 열 저장
# 1-1. 포함된 열 별로 사이즈 합하여 저장
# 2. #1-1의 최댓값 리턴

from collections import deque

def bfs(x, y, n, m, visited, land):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    cnt = 0
    area = set()
    while queue:
        qx, qy = queue.popleft()
        cnt += 1
        area.add(qx)
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx] and land[ny][nx] != 0:
                visited[ny][nx] = True
                queue.append((nx, ny))
    return cnt, area

def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    ans = [0] * m
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] != 0:
                size, area = bfs(j, i, n, m, visited, land)
                for a in area:
                    ans[a] += size
    return max(ans)