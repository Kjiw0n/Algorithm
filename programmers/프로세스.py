from collections import deque

def solution(priorities, location):
    queue = deque()
    for i, priority in enumerate(priorities):
        queue.append((priority, i))
    
    priorities.sort(reverse=True)
    priorities = deque(priorities)
    cnt = 0
    while queue:
        process, i = queue.popleft()
        if process >= priorities[0]:
            priorities.popleft()
            cnt += 1
            if i == location: return cnt
        else:
            queue.append((process, i))
