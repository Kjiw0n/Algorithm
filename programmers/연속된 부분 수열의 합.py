# 조건을 만족하는 배열의 시작 인덱스, 마지막 인덱스 리턴

# 1. 순서대로 원소 더하기
# 2. k를 넘으면 앞에서부터 빼기
# 3. k에 도달하면 ans에 시작/마지막 인덱스 저장해두고, min_length도 저장해두기
# 3-1. min_length 미만인 경우만 ans 업뎃

# N = 10^6, M = 10^9, O(2 * N)

from collections import deque

def solution(sequence, k):
    queue = deque()
    total = 0
    ans = []
    min_length = float('inf')
    for i, n in enumerate(sequence):
        if n > k: break
        while total + n > k and queue:
            idx = queue.popleft()
            total -= sequence[idx]
            
        total += n
        queue.append(i)
        
        if total == k:
            s, e = queue[0], queue[-1]
            if e - s + 1 < min_length:
                ans = [s, e]
                min_length = e - s + 1
    
    return ans