import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

queue = deque()
for _ in range(N):
    cmd = list(input().rstrip().split())
    if cmd[0] == 'push_front':
        queue.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        queue.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if queue:
            print(str(queue.popleft()) + '\n')
        else:
            print(str(-1) + '\n')
    elif cmd[0] == 'pop_back':
        if queue:
            print(str(queue.pop()) + '\n')
        else:
            print(str(-1) + '\n')
    elif cmd[0] == 'size':
        print(str(len(queue)) + '\n')
    elif cmd[0] == 'empty':
        if queue:
            print(str(0) + '\n')
        else:
            print(str(1) + '\n')
    elif cmd[0] == 'front':
        if queue:
            print(str(queue[0]) + '\n')
        else:
            print(str(-1) + '\n')
    elif cmd[0] == 'back':
        if queue:
            print(str(queue[-1]) + '\n')
        else:
            print(str(-1) + '\n')