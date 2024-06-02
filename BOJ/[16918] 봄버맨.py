import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
graph = []
for i in range(R):
    graph.append(list(input().strip()))

# 터질 곳을 미리 기억해둬야한다?
# 200개밖에 안되기때문에 순회 가능하긴 함
# 근데 그렇다고 매번 순회?
# 흐으음
# 아하 다시 돌아오네
#
# 만들어지는 경우는 4가지
# 초기상태
# 전부 폭탄
# 전부 폭탄에서 초기 폭탄들만 터진 상태
# (다시) 전부 폭탄
# 초기 폭탄 터지고 전부 폭탄도 터짐?
# (반복)

def print_graph(graph):
    for g in graph:
        print(''.join(g))

def bomb(graph):
    new_graph = [['O'] * C for _ in range(R)]
    dx = [0, 0, 0, -1, 1]
    dy = [0, -1, 1, 0, 0]
    for x in range(R):
        for y in range(C):
            if graph[x][y] == 'O':
                for d in range(5):
                    nx, ny = x + dx[d], y + dy[d]
                    if 0 <= nx < R and 0 <= ny < C:
                        new_graph[nx][ny] = '.'
    return new_graph

if N == 1:
    # 초기상태
    print_graph(graph)
elif N % 2 == 0:
    # 전부 폭탄
    all = [['O'] * C for _ in range(R)]
    print_graph(all)
elif N % 4 == 3:
    # 전부 폭탄에서 초기 폭탄들만 터진 상태
    print_graph(bomb(graph))
else:
    # N % 4 == 1
    # 초기 터지고 모든 폭탄 또 터짐
    print_graph(bomb(bomb(graph)))
