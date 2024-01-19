import sys

N = int(sys.stdin.readline())

# 증가 버전
for i in range(N):
    star_n = 2 * i + 1
    #      = 홀수 증가
    #      = 2i + 1 (i는 0부터 증가니까)
    space_n = N - (i + 1)

    for _ in range(space_n):
        sys.stdout.write(' ')
    for _ in range(star_n):
        sys.stdout.write('*')
    print()

# 감소 버전
for i in range(N - 1, 0, -1):
    star_n = 2 * i - 1
    space_n = N - i

    for _ in range(space_n):
        sys.stdout.write(' ')
    for _ in range(star_n):
        sys.stdout.write('*')
    print()