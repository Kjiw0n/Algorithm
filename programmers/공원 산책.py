# 1. 시작 지점 좌표 찾기
# 2. 명령어에 따라 이동
# 2-1. op에 따른 이동 저장해두기
# 3. 현재 위치 리턴

def solution(park, routes):
    pos = [0, 0]
    H = len(park)
    W = len(park[0])
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                pos = [i, j]
                
    # N, S, W, E
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    d = 0
    for route in routes:
        op, n = route.split(' ')
        if op == 'N': d = 0
        elif op == 'S': d = 1
        elif op == 'W': d = 2
        else: d = 3
        
        flag = True
        y, x = pos
        for _ in range(int(n)):
            nx = x + dx[d]
            ny = y + dy[d]
            print(nx, ny)
            if 0 <= nx < W and 0 <= ny < H and park[ny][nx] != 'X':
                y, x = ny, nx
            else: 
                flag = False
                break
        
        if flag: 
            y, x = pos
            x = x + (dx[d] * int(n))
            y = y + (dy[d] * int(n))
            pos = [y, x]
        
    return pos