from collections import deque

def solution(numbers, target):
    queue = deque([0])

    for num in numbers:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            queue.append(cur + num)
            queue.append(cur - num)

    return queue.count(target)