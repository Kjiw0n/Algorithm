import sys
from collections import deque

input = sys.stdin.readline().rstrip

N = int(input())

nums = list(range(N, 0, -1))
queue = deque(nums)

n = 0
while queue:
    # 1. 버림
    n = queue.pop()
    # 2. 맨 위 카드를 맨 밑으로 옮기기
    if queue:
        move = queue.pop()
        queue.appendleft(move)

print(n)