import math

N = int(input())

length = 2 * N
graph = [[' '] * length for _ in range(length)]

# 이번에도 시작점을 집고
# 각 시작점 기점으로 세모 그리기
# 시작점은 세모의 꼭짓점
#
# x, y 라고 할 때
#
# 1) x, y
# 2) x - (N // 2), y + 3 * (2^k // 2)
# 3) x + (N // 2) - 1, y + 3 * (2^k // 2)

star = '*'
def recursion(x, y, N):
    k = round(math.log2(N // 3))

    if N == 3:
        # 별 찍고 종료
        graph[y][x] = star
        graph[y + 1][x - 1] = star
        graph[y + 1][x + 1] = star
        for i in range(5):
            graph[y + 2][x - 2 + i] = star
        return

    n = N // 2
    dx = N // 2
    dy = 3 * (2 ** (k - 1))
    recursion(x, y, n)
    x1 = x - dx
    x2 = x + dx
    y1 = y + dy
    recursion(x1, y1, n)
    recursion(x2, y1, n)


recursion(N - 1, 0, N)
for i in range(length):
    print(''.join(graph[i]))
