# 2 * N 줄 출력
# 홀수줄 -> 1 1 2 2 3 3
#   1, 3, 5 될때마다 +1
#   (N-1) // 2 + 1
# 짝수줄 -> 0 1 1 2 2
# 2, 4, 6 될때마다 +1
#   N // 2

import sys

N = int(sys.stdin.readline())


def odd(n):
    n = (n - 1) // 2 + 1
    result = '* ' * n
    return result


def even(n):
    n = n // 2
    result = (' ' + ('* ' * n))
    return result


for _ in range(N):
    print(odd(N))
    print(even(N))
