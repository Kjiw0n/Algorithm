import sys

N = int(sys.stdin.readline())

for i in range(N, 0, -1):
    for _ in range(i):
        sys.stdout.write('*')
    print()