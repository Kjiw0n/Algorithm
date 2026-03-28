# Todo: 붕대 감기 기술 사용을 통한 체력 구하기
# return: 몬스터의 모든 공격 후 남은 체력, 캐릭터가 죽으면 -1 리턴

# 1. 시간 1초마다 올리면서 체크
# 2. 1초마다 붕대감기 시간 증가 
# 2-1. 체력 회복 및 기술 성공 여부 체크
# 3. attacks 앞에서부터 확인, 공격 시간 도달하면 체력 제거 및 붕대감기 초기화
# 4. 공격이 모두 끝나면 게임 종료

# N: 공격시간(=1,000), O(N) 완탐 가능

from collections import deque

def solution(bandage, health, attacks):
    t = 0
    bandageT = 0
    attacks = deque(attacks)
    attackT, attackP = attacks.popleft()
    
    now = health
    
    while t <= attackT:
        # 공격 받음
        if t == attackT:
            now -= attackP
            bandageT = 0
            if attacks :
                attackT, attackP = attacks.popleft()
        else:
            bandageT += 1
            now = min(health, now + bandage[1])
        
        # 기술 사용
        if bandageT == bandage[0]:
            now = min(health, now + bandage[2])
            bandageT = 0
        
        # 시간 증가
        t += 1
        
        if now <= 0: return -1
    
    return now