import sys
input = sys.stdin.readline

T = int(input())

dp = [0] * (100001)
dp[1] = 1
dp[2] = 2
dp[3] = 2
dp[4] = 3
dp[5] = 3
dp[6] = 6
dp[7] = 6
dp[8] = 11

for i in range(8, 100001):
    dp[i] = (dp[i - 2] + dp[i - 4] + dp[i - 6]) % 1000000009

for _ in range(T):
    n = int(input())
    print(dp[n])