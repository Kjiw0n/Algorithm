import sys

N = int(sys.stdin.readline())

for i in range(N):
    star_n = 2 * (i + 1) - 1
    space_n = N - (i + 1)
    for _ in range(space_n, 0, -1):
        sys.stdout.write(' ')
    for _ in range(star_n):
        sys.stdout.write('*')
    print()