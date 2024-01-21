import sys

N = int(sys.stdin.readline())

star = '* '
space = ' '

for i in range(N):
    if i % 2 != 0:
        sys.stdout.write(space)
    sys.stdout.write(star * N)
    print()
