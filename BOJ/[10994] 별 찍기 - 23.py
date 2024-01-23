import sys

# 2 -> 1, 5 -> 7 => 2(N-1) - 1

# 5일때
# 7
# 5
# 3
# 1
# 0 (얘가 중간. N번째 줄)

# 맨 처음 + 맨 마지막 -> * N개 + mid_space(= 2(N-1) - 1) + * N개
# 중간 -> space(= i) + '*{N-2}*' + mid_space + '*{N-2}*'

N = int(sys.stdin.readline())

edge = '*' * N + ' ' * (2 * (N - 1) - 1) + '*' * N
mid_star = '*' + ' ' * (N - 2) + '*'

for i in range(N):
    first_space = ' ' * i
    mid_space = ' ' * (2 * (N - 1 - i) - 1)

    if i == 0:
        print(edge)
    elif i == N - 1:
        print(first_space + mid_star + ' ' * (N - 2) + '*')
    else:
        sys.stdout.write(first_space + mid_star + mid_space + mid_star)
        print()


for i in range(N - 1, 0, -1):
    first_space = ' ' * (i - 1)
    mid_space = ' ' * (2 * (N- i) - 1)

    if i == 1:
        print(edge)
    else:
        sys.stdout.write(first_space + mid_star + mid_space + mid_star)
        print()
