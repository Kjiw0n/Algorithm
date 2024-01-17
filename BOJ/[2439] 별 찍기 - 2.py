import sys

N = int(sys.stdin.readline())

for i in range(N):
    n = N - (i + 1)
    for _ in range(n):
        sys.stdout.write(' ')
    for _ in range(N - n):
        sys.stdout.write('*')
    i += 1
    print()