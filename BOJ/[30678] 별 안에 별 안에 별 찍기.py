import sys

sys.setrecursionlimit(10**6)

N = int(input())

# width, height: 5 ** N
length = 5 ** N
graph = [[' '] * length for _ in range(length)]

# 시작점만 찾기
# N == 1일때 별 그리고 리턴
star = '*'
def recursion(x, y, N):
    if N == 1:
        graph[y][x] = star
        graph[y + 1][x] = star
        for i in range(5):
            dx = x - 2 + i
            graph[y + 2][dx] = star
        for i in range(3):
            dx = x - 1 + i
            graph[y + 3][dx] = star
        graph[y + 4][x - 1] = star
        graph[y + 4][x + 1] = star
        return

    n = 5 ** (N - 1)
    recursion(x, y, N - 1)
    recursion(x, y + n, N - 1)
    for i in range(5):
        dx = x - n * 2 + i * n
        recursion(dx, y + n * 2, N - 1)
    for i in range(3):
        dx = x - n + i * n
        recursion(dx, y + n * 3, N - 1)
    recursion(x - n, y + n * 4, N - 1)
    recursion(x + n, y + n * 4, N - 1)

if N == 0:
    print('*')
else:
    x = (length - 1) // 2
    recursion(x, 0, N)

    for i in range(length):
        print(''.join(graph[i]))