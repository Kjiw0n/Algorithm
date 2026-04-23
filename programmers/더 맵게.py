# 스코빌 지수 K 이상으로 만들기 위한 최소 섞는 횟수 리턴

# 1. scoville 우선순위큐에 넣기
# 2. 가장 작은 원소, 두번째로 작은 원소 꺼내서 계산 후 큐에 추가, 횟수 + 1
# 2-1. 두개를 꺼낼 수 없다면 -1 리턴
# 3. scoville의 최솟값이 K 미만인 경우 #2 반복

# N = 10^6, O(N)

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    while scoville[0] < K:
        if len(scoville) == 1: return -1
    
        s1 = heapq.heappop(scoville)
        s2 = heapq.heappop(scoville)
        heapq.heappush(scoville, s1 + s2 * 2)
        cnt += 1
    
    return cnt