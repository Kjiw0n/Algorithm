# 9
# 1 1 1 1 1 1 1 1 1 -> 1개
# 2 1 1 1 1 1 1 1   -> 8개
# 2 2 1 1 1 1 1     -> 21개 7! / 2!, 5!
# 2 2 2 1 1 1       -> 20개 6! / 3!, 3!
# 2 2 2 2 1         -> 5개

import sys

sys.setrecursionlimit(10 ** 6)

N = int(input())

# n 을 1과 2로 구성하는 법은?
# (이때 2로 구성하는 경우엔 위에도 쌓임 2층으로 -> 이러면 걍 1개라고 쳐도..?)

# N - 2 * i 로 몫을 하나씩 늘려가고, 나머지는 어차피 1로 처리할거니까 모두 개수처리
# 2 i개, 1 (N - 2 * i)개
# 순서는 중복 알아서 처리하기 (: C)

dp = [0] * (N + 1)
dp[0] = 1
def factorial(n):
    if dp[n] == 0:
        dp[n] = n * factorial(n - 1)
        # print('dp[', n, ']: ', dp[n])
    return dp[n]

result = 0
for i in range(N // 2 + 1):
    count1 = N - (2 * i)

    result += factorial(i + count1) // (factorial(i) * factorial(count1))

print(result % 10007)
