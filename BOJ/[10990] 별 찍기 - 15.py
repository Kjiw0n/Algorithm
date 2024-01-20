import sys

N = int(sys.stdin.readline())

for i in range(N):
    first_space = ' ' * (N - (i + 1))
    if i == 0:
        sys.stdout.write(first_space + '*')
        print()
    else:
        mid_space = 2 * i - 1
        sys.stdout.write(first_space + '*' + ' ' * mid_space + '*')
        print()
