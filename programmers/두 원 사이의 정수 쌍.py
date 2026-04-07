# 두 원 사이에 있는 좌표 중, x, y가 모두 정수인 좌표 개수

# 1. 좌표축 위의 점은 따로 카운트
# 1-1. 1차원의 좌표만 카운트 후 *4
# 2. x일때의 y1, y2를 구한 후 그 사이의 정수 계산

# N = 1,000,000, O(N)

import math

def Y1(r1, x):
    if x < r1:
        y1 = math.ceil((r1 ** 2 - x ** 2) ** 0.5)
    else:
        y1 = 0
    return y1

def solution(r1, r2):
    y1 = 0
    y2 = 0
    cnt = 0
    for x in range(r2):
        y1 = Y1(r1, x)
        y2 = math.floor((r2 ** 2 - x ** 2) ** 0.5)
        if y1 == 0: y1 = 1
        cnt += y2 - y1 + 1
    return cnt * 4