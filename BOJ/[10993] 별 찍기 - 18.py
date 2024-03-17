# graph 만들고
# 시작점 찾기
# n 이 짝수냐 홀수냐에 따라 시작점으로부터 위로 찍을 지 아래로 찍을 지 정하기

# 1 -> 1
# 2 -> (1 + 2) * 2 - 1
# 3 -> (5 + 2) * 2 - 1

# 2 5 3
# 3 13 7
# 4 29 15

N = int(input())

width = [1]
height = [1]
for i in range(N - 1):
    width.append((width[-1] + 2) * 2 - 1)
    height.append((height[-1] * 2 + 1))

graph = [[' '] * width[-1] for _ in range(height[-1])]

star = '*'
def recursion(x, y, N):
    graph[y][x] = star
    if N == 1:
        return

    if N % 2 != 0:
        lx, ly = x, y
        rx, ry = x, y
        for i in range(height[N - 1] - 1):
            lx -= 1
            ly += 1
            rx += 1
            ry += 1
            if i == height[N - 1] - 2: # 마지막줄
                for _ in range(width[N - 1]):
                    graph[ly][lx] = star
                    lx += 1
                break
            graph[ly][lx] = star
            graph[ry][rx] = star
        recursion(x, y + height[N - 1] - 2, N - 1)
    else:
        lx, ly = x, y
        rx, ry = x, y
        for i in range(height[N - 1] - 1):
            lx -= 1
            ly -= 1
            rx += 1
            ry -= 1
            if i == height[N - 1] - 2: # 마지막줄
                for _ in range(width[N - 1]):
                    graph[ly][lx] = star
                    lx += 1
                break
            graph[ly][lx] = star
            graph[ry][rx] = star
        recursion(x, y - height[N - 1] + 2, N - 1)


# # 처음 시작점
# # N 짝수 -> 시작점: x = width[N - 1] // 2 + 1, y = height[N - 1]
# N 홀수 -> 시작점: x = width[N - 1] // 2 + 1, y = 0

fx = width[N - 1] // 2
fy = height[N - 1] - 1
if N % 2 == 0:
    recursion(fx, fy, N)
else:
    recursion(fx, 0, N)
for i in range(height[-1]):
    print(''.join(graph[i]).rstrip())

