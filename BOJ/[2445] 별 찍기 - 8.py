import sys

N = int(sys.stdin.readline())

# 일단 증가부분부터
# 앞쪽 별 출력 -> 공백 2배 해서 출력 -> 다시 앞에 찍은만큼 별
for i in range(N):
    star_n = i + 1
    # star_n 은 걍 1~5까지 증가함
    space_n = (N - (i + 1)) * 2

    for _ in range(star_n):
        sys.stdout.write('*')
    for _ in range(space_n):
        sys.stdout.write(' ')
    for _ in range(star_n):
        sys.stdout.write('*')
    print()

# 감소 부분
for i in range(N-1, 0, -1):
    # 여기서 star_n 은 걍 i
    space_n = (N - i) * 2

    for _ in range(i):
        sys.stdout.write('*')
    for _ in range(space_n):
        sys.stdout.write(' ')
    for _ in range(i):
        sys.stdout.write('*')
    print()