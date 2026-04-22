# 아이템을 줍기 위한 최소 이동 거리 리턴

# 1. 지형 분석 -> 50x50 graph 0으로 초기화
# 1-1. 간격 조정을 위해 사각형 좌표 각각 2배
# 1-2. [lx, ly, rx, ry] 사각형 둘레를 1로 처리
# 1-3. 사각형 내부는 -1로 처리
# 1-4. 다음 사각형 둘레 처리 시, -1인 곳은 1 처리 패쓰, 0인 곳만 1 처리
# 2. 지형에 따라 최소 거리로 이동하여 아이템 줍기
# 2-1. graph에서 1인 곳으로만 이동했을 때 최소 거리인 경우 찾기

from collections import deque

N = 102

def bfs(cX, cY, itemX, itemY, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    queue.append((cX, cY, cnt))
    visited[cY][cX] = True
    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == (itemX, itemY): 
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 < nx < N and 0 < ny < N and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny, cnt + 1))
    return cnt
                

def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[0] * N for _ in range(N)]
    for lx, ly, rx, ry in rectangle:
        lx, ly, rx, ry = lx * 2, ly * 2, rx * 2, ry * 2
        # 테두리 처리
        for x in [lx, rx]:
            for y in range(ly, ry + 1):
                if graph[y][x] != -1:
                    graph[y][x] = 1
        for y in [ly, ry]:
            for x in range(lx, rx + 1):
                if graph[y][x] != -1:
                    graph[y][x] = 1
        
        # 내부 처리
        for x in range(lx + 1, rx):
            for y in range(ly + 1, ry):
                graph[y][x] = -1
        
    return bfs(characterX * 2, characterY * 2, itemX * 2, itemY * 2, graph) // 2
