# 전부 요격시키기 위한 요격 미사일 수의 최솟값 리턴

# 1. targets 오름차순 정렬 (e 지점 기준)
# 1-1. 실수 계산 어려우니까 targets의 모든 s, e에 두배
# 2. i번째 타겟이 없어지기 직전에 쏘기 -> (spot == e - 1)일때
# 3. (i + 1)번째 타겟이 spot보다 나중에 시작했으면 다시 쏘기

# N = 5 * 10^5(: target), M = 10^8, O(N)

def solution(targets):
    targets.sort(key=lambda x: x[1])
    targets = [[s * 2, e * 2] for s, e in targets]
    
    spot = -1
    cnt = 0
    for i, target in enumerate(targets):
        if spot < target[0]:
            # 요격 미사일 쏘기
            spot = target[1] - 1
            cnt += 1
    
    return cnt