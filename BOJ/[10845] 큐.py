from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

queue = deque()
for _ in range(N):
    s = input().split()

    if s[0] == 'push':
        queue.append(s[1])
    elif s[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(queue))
    elif s[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if queue:
            print(queue[len(queue) - 1])
        else:
            print(-1)