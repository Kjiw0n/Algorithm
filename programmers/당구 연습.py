# 각 회마다 공이 굴러간 거리의 최솟값의 제곱 리턴

# 1. balls 위치 반사시켜서 직선거리 구하기
# 2. 벽에 닿기 전에 공을 먼저 맞추는 경우는 제외
# 2-1. 다음 경우는 제외
# (a, 10) -> Ax == Tx and Ay < Ty < 10
# (10, b) -> Ay == Ty and Ax < Tx < 10
# (a, 0) -> Ax == Tx and 0 < Ty < Ay
# (0, b) -> Ay == Ty and 0 < Tx < Ax

def calculator(sX, sY, bX, bY):
    return (sX - bX) ** 2 + (sY - bY) ** 2

def solution(m, n, startX, startY, balls):
    ans = []
    for bX, bY in balls:
        distances = []
        # (a, 10)
        if not (startX == bX and startY < bY < n):
            distances.append(calculator(startX, startY, bX, 2 * n - bY))
        
        # (10, b)
        if not (startY == bY and startX < bX < m):
            distances.append(calculator(startX, startY, 2 * m - bX, bY))
        
        # (a, 0)
        if not (startX == bX and 0 < bY < startY):
            distances.append(calculator(startX, startY, bX, -bY))
        
        # (0, b)
        if not (startY == bY and 0 < bX < startX):
            distances.append(calculator(startX, startY, -bX, bY))
        
        ans.append(min(distances))
        
    return ans