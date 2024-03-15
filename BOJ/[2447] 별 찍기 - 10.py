# 크기에 맞는 map(리스트) 선언 후 좌표로 찍기..

# 크기 N의 패턴은
# 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을
# 크기 N/3의 패턴으로 둘러싼 형태


str1 = '***************************'
print(str1.count('*'))

N = int(input())
graph = [['*'] * N for _ in range(N)]

# 공백만 찾아서 처리?
# 가운데만 공백임
# 각 네모의 시작점을 제공해주면? -> !!
def recursion(x, y, N):
    if N == 1:
        return

    # +9, +9 시점부터 공백 +9, +9 -> 공백은 시작점의 x + N/3, y + N/3
    # N/3인 각 네모의 시작점은

    n = N // 3

    for i in range(3):
        for j in range(3):
            dx = x + (n * i)
            dy = y + (n * j)
            if i == 1 and j == 1:
                # 공백화
                for a in range(n):
                    for b in range(n):
                        graph[dx+a][dy+b] = ' '
            else:
                recursion(dx, dy, n)

    # x + (N / 3) * 0, y + (N / 3) * 0
    # x + (N / 3) * 0, y + (N / 3) * 1
    # x + (N / 3) * 0, y + (N / 3) * 2
    #
    # x + (N / 3) * 1, y + (N / 3) * 0
    # x + (N / 3) * 1, y + (N / 3) * 1
    # x + (N / 3) * 1, y + (N / 3) * 2
    #
    # x + (N / 3) * 2, y + (N / 3) * 0
    # x + (N / 3) * 2, y + (N / 3) * 1
    # x + (N / 3) * 2, y + (N / 3) * 2

recursion(0,0 , N)

for i in range(N):
    print(''.join(graph[i]))