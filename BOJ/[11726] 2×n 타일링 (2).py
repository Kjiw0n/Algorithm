import sys

sys.setrecursionlimit(10**6)

n = int(input())

dp = [0] * (n + 1) # 팩토리얼 담기
dp[0], dp[1] = 1, 1
def fac(n):
    if dp[n] == 0:
        dp[n] = n * fac(n - 1)
    return dp[n]

result = 0
i = 0
while n >= i * 2:
    result += fac(n - i) // (fac(n - (i * 2)) * fac(i))
    i += 1

print(result % 10007)
