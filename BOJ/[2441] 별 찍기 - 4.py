import sys

N = int(sys.stdin.readline())

for i in range(N):
    n = N - i
    for _ in range(i):
        sys.stdout.write(' ')
    for I in range(n):
        sys.stdout.write('*')
    print()