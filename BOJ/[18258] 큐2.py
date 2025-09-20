import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    command = list(input().split())

    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        if queue:
            sys.stdout.write(str(queue.popleft()) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')

    elif command[0] == 'size':
        sys.stdout.write(str(len(queue)) + '\n')
    elif command[0] == 'empty':
        if queue:
            sys.stdout.write(str(0) + '\n')
        else:
            sys.stdout.write(str(1) + '\n')
    elif command[0] == 'front':
        if queue:
            sys.stdout.write(str(queue[0]) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')
    elif command[0] == 'back':
        if queue:
            sys.stdout.write(str(queue[-1]) + '\n')
        else:
            sys.stdout.write(str(-1) + '\n')
