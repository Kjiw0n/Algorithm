def solution(brown, yellow):
    ans = []

    brown -= 4
    brown //= 2

    for i in range(1, brown):
        if i * (brown - i) == yellow:
            ans = [i, brown - i]

    ans.sort(reverse=True)

    return [ans[0] + 2, ans[1] + 2]
# 모서리 4개 빼고,

# 8 - 4 = 4, 4 / 2 = 2
# x + y = 2, x * y = 1 -> x=1, y=1

# 24 - 4 = 20, 20 / 2 = 10
# x + y = 10, x * y = 24 -> x=6, y=4

# x + y = brown, x * y = yellow
# y = brown - x, x * (brown - x) = yellow