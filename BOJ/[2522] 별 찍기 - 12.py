import sys

N = int(sys.stdin.readline())

for i in range(N):
    space_n = N - (i + 1)

    sys.stdout.write(' ' * space_n)
    sys.stdout.write('*' * (i + 1))
    print()

for i in range(N - 1, 0, -1):
    space_n = N - i

    sys.stdout.write(' ' * space_n)
    sys.stdout.write('*' * i)
    print()