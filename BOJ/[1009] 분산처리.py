# a^b / 10 의 나머지
# 시간초과 - ** 때문
# 2 4 8 16 32 64 128
# 3 9 7 1 3
# 4 6 4
# 5 5 5 5
# 6 6 6
# 7 9 3 1 7
# 규칙..

# b가 반복 주기를 찾지 못할만큼 작은 경우 -> 바로 계산

from sys import stdin

T = int(stdin.readline().strip())

def exp_func(a, b):
    # a^i == a^j 인 거 나오면 저장x 하고 break
    # 반복 주기 가진 리스트 return
    exp = []

    for i in range(b):
        n = (a ** (i + 1)) % 10
        exp.append(n)

        for j in range(i):
            if exp[i] == exp[j]:
                return exp[:i]


for i in range(T):
    a, b = map(int, stdin.readline().strip().split())

    exp = exp_func(a, b)
    result = 0
    if exp is None:
        result = (a ** b) % 10
    else:
        last_index = (b - 1) % len(exp)
        result = exp[last_index]

    print(result if result != 0 else 10)
