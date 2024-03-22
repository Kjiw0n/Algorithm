from itertools import combinations

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    # 최대 -> 동쪽에서 N개 고르면 끝
    # 1. 조합 -> 시간 너무 오래걸림
    # temp = list(range(1, M + 1))
    # comb = list(combinations(temp, N))
    #
    # result.append(len(comb))

    # 2. 그냥 계산하기
    # result.append(factorial(M) // (factorial(a[1] - a[0]) * factorial(N)))

    # 3. 그냥 dp로 해야할듯
    # 위에서 아래로
    dp = [0] * (M + 1) # 펙토리얼 계산한 값 담을거임
    dp[0] = 1
    dp[1] = 1

    def factorial(n):
        if dp[n] == 0:
            dp[n] = n * factorial(n - 1)
        return dp[n]

    print(factorial(M) // (factorial(M - N) * factorial(N)))




