N, r, c = map(int, input().split())

# Z의 시작점만 찾으면 됨. (2 ** N) / 2 하면 됨
# s: 시작점
# n: Z의 사이즈
# result: 방문 횟수
def draw_z(s, n, result):
    if n == 1:
        print(result)
        return

    dn = n // 2

    if r < s[0] + dn and c < s[1] + dn:
        # Q2만 탐색
        start = [s[0], s[1]]
        draw_z(start, dn, result)
    elif r >= s[0] + dn and c < s[1] + dn:
        # Q3
        start = [s[0] + dn, s[1]]
        result += (dn ** 2) * 2
        draw_z(start, dn, result)
    elif r < s[0] + dn and c >= s[1] + dn:
        # Q1
        start = [s[0], s[1] + dn]
        result += dn ** 2
        draw_z(start, dn, result)
    elif r >= s[0] + dn and c >= s[1] + dn:
        # Q4
        start = [s[0] + dn, s[1] + dn]
        result += (dn ** 2) * 3
        draw_z(start, dn, result)

draw_z([0, 0], 2 ** N, 0)
