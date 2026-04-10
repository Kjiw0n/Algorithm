# 1. 각 위치 별 고를 수 있는 최댓값 구하기
# 2. #1 누적

def solution(triangle):
    for h in range(len(triangle) - 2, -1, -1):
        for i in range(len(triangle[h])):
            triangle[h][i] += max(triangle[h+1][i], triangle[h+1][i+1])
    
    return triangle[0][0]