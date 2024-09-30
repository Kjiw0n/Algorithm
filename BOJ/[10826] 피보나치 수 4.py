# n = int(input())
#
# dp = [0] * (n + 3)
# dp[1] = 1
# dp[2] = 1
#
# if n == 0:
#     print(dp[0])
# else:
#     for i in range(3, n + 2):
#         if dp[i] == 0:
#             dp[i] = dp[i - 1] + dp[i - 2]
#
#     print(dp[n])

# 개선 버전
n = int(input())

x = 0
y = 1
for _ in range(n):
    x, y = y, x + y

print(x)