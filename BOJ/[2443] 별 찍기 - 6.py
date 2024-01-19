import sys

N = int(sys.stdin.readline())

for i in range(N):
    star_n = 2 * (N - i) - 1
    #      = 2 * N - (2 * (i + 1) - 1)
    #      = 2N - (2i + 1)
    #      = 2N - 2i - 1
    #      = 2(N - i) - 1

    for _ in range(i):
        sys.stdout.write(' ')
    for _ in range(star_n, 0, -1):
        sys.stdout.write('*')
    print()