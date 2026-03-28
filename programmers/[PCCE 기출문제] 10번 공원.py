# Todo: 정사각형 모양 돗자리를 까는 경우의 수
# return: 가장 큰 돗자리의 한 변 길이, 깔 수 없는 경우 -1

# 1. 지민이가 가진 돗자리 중, 큰 것 부터 체크
# 2. 비어있는 자리 마다 정사각형 경로로 체크
# 2-1. 정사각형 넓이만큼 탐색하면 해당 돗자리 리턴
# 2-2. 정사각형 넓이만큼 탐색 못하면 다음 돗자리로 넘어감(#2 반복)

# 50 * 50 * 20 * 20 = 1000 * 1000 = 완탐 가능

from collections import deque

# 정사각형 반경 탐색, (x, y)가 항상 시작점(왼쪽상단)이라고 판단
def bfs(M, N, x, y, mat, park):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * M for _ in range(N)]
    
    queue = deque()
    queue.append((x, y))
    visited[y][x] = True
    
    area = set()
    area.add((x, y))
    
    while queue:
        qx, qy = queue.popleft()
        if len(area) == mat * mat:
            return True
        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]
            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and park[ny][nx] == '-1':
                visited[ny][nx] = True
                if x <= nx < x + mat and y <= ny < y + mat:
                    # 정사각형 내부
                    area.add((nx, ny))
                    queue.append((nx, ny))
    
    return False
    
def solution(mats, park):
    N = len(park)
    M = len(park[0])   
    
    mats.sort(reverse = True)
    
    for mat in mats:
        for y in range(N):
            for x in range(M):
                if park[y][x] == '-1':
                    if bfs(M, N, x, y, mat, park):
                        return mat
    
    return -1