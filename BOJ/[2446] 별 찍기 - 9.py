import sys

N = int(sys.stdin.readline())

# 감소 부분
for i in range(N - 1):
    star_n = 2 * (N - i) - 1
    #      = 2N - 1부터 홀수/감소
    #      = 2N - (2i + 1) (i는 0부터)
    #      = 2N - 2i - 1
    #      = 2(N - i) - 1
    # space_n = i

    for _ in range(i):
        sys.stdout.write(' ')
    for _ in range(star_n, 0, -1):
        sys.stdout.write('*')
    print()

# 증가
for i in range(N):
    star_n = 2 * i + 1
    #      = 홀수 증가
    space_n = N - (i + 1)

    for _ in range(space_n):
        sys.stdout.write(' ')
    for _ in range(star_n):
        sys.stdout.write('*')
    print()
