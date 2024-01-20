# '*' 먼저 찍고, 줄바꿈 전에 ' *' * 줄넘버 - 1

import sys

N = int(sys.stdin.readline())

for i in range(N):
    first_space = ' ' * (N - (i + 1))
    sys.stdout.write(first_space + '*')
    sys.stdout.write(' *' * i)
    print()