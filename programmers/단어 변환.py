# begin->target 변환 최소 단계 리턴, 변환 불가 시 0 리턴

# 1. begin과 한 글자만 차이나는 단어로 변환
# 1-1. 그 단어가 여러 개라면 모두 queue에 저장
# 2. #1 반복, target에 도달 시 해당 단계 리턴
# 3. 끝까지 target 도달 못하면 0 리턴

from collections import deque

def solution(begin, target, words):
    if target not in words: return 0

    queue = deque()
    visited = [False] * len(words)
    queue.append((begin, 0))
    while queue:
        cur, cnt = queue.popleft()
        if cur == target:
            return cnt
        
        for i, word in enumerate(words):
            if not visited[i]:
                diff = 0
                for c, w in zip(cur, word):
                    if c != w: diff += 1
                if diff == 1:
                    queue.append((word, cnt + 1))
                    visited[i] = True
    
    return 0