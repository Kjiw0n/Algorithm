# 1 ~ N-1번째 줄까지는 별찍기16처럼 풀고
# if N번째줄: print('*' * (2N+1))

import sys

N = int(sys.stdin.readline())

for i in range(N):
    if i == N - 1:
        last_line = '*' * (2 * N - 1)
        sys.stdout.write(last_line)
        break

    first_star = ' ' * (N - (i + 1)) + '*' # i+1번째 줄
    sys.stdout.write(first_star)
    if i != 0:
        second_star = ' ' * (2 * i - 1) + '*' # 띄어쓰기 = ' ' * 홀수
        sys.stdout.write(second_star)
    print()