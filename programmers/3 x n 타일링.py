def solution(n):
    # 직사각형 넓이 = 3 * n
    # 타일 넓이 = 1 * 2
    # -> n은 무조건 짝수

    # n = 2 -> 3가지
    # n = 4 -> 11가지 = 3 * 3 + 2
    #
    # 점화식 세워야하니까 n = 0 있다고 가정...
    # n = 0일때 dp[0] = 1이면
    # dp[2] = dp[0] * 3 = 3
    # dp[4] = dp[2] * 3 + dp[0] * 2 = 11

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3
    dp[4] = 11
    for i in range(2, n // 2 + 1):
        # print(i * 2, (i-1) * 2, 2*(i-2) + 1, dp[:2*(i-2) + 1])
        dp[i * 2] = dp[(i-1) * 2] * 3 + 2 * (sum(dp[:2*(i-2) + 1]))

    print(dp[n])


    answer = dp[n] % 1000000007
    return answer

print(solution(8))