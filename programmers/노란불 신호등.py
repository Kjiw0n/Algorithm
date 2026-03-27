# Todo: 모든 신호등이 노란불이 되는 경우 찾기
# return: 모든 신호등이 노란불이 되는 가장 빠른 시각, 없으면 -1

# 1. 전체 주기(: 각 주기의 최소공배수) 구하기
# 2. 전체 주기만큼 1초씩 돌려가며 체크
# 2-1. 각 신호등 하나씩 돌려가며 색 체크
# 2-2. 각 초마다 노란불 카운팅 -> 전부 노란불인지 체크
# 2-3. 초 바뀌면 노란불 카운팅 초기화

# 시간 복잡도 O(최소공배수 * N)

import math

def get_lcm(a, b):
    return (a * b) // math.gcd(a, b)

def solution(signals):
    N = len(signals) # 신호등 개수
    cycles = [sum(sig) for sig in signals]
    
    LCM = cycles[0]
    for i in range(1, len(cycles)):
        LCM = get_lcm(LCM, cycles[i])
    
    arr = []
    for sig in signals:
        a = [0] * sig[0] + [1] * sig[1] + [0] * sig[2]
        arr.append(a)
        
    for time in range(LCM):
        cnt = 0
        for a , cycle in zip(arr, cycles):
            if a[time % cycle] == 1: cnt += 1
        if cnt == N:
            return time + 1
            
    return -1