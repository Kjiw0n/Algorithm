N = int(input())

d = [0] * (N + 1)


def fibonachi(n):
    if n == 1 or n == 2:
        return 1

    if d[n] != 0:
        # 이미 계산한 적 있으면 바로 반환
        return d[n]

    d[n] = fibonachi(n - 1) + fibonachi(n - 2)
    return d[n]

print(fibonachi(N))