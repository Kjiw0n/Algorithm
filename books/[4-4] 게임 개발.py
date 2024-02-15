# s 20:50 (40분)
# e 21:50 (+ 20분x)
#
# N x M: 각 칸은 육지(0), 바다(1)
# (0, 0)  (0, M)
#
# (N, 0)  (N, M)
#
# 방향이 있다?
# 왼쪽 안가본 곳이면 이동, 가본 곳이면 왼쪽으로 방향만 틀기
# 모든 방향이 이미 가봄 or 바다 -> 방향 유지한채로 1칸 뒤로 감 if 뒷칸 바다: 그만가
#
# 방문한 칸 수 출력

N, M = map(int, input().split())
A, B, d = map(int, input().split())

visit = [[0] * M for _ in range(N)]
visit[A][B] = 1

game_map = [[0] * M for _ in range(N)]
for i in range(N):
    game_map[i] = list(map(int, input().split()))

# N(0), E(1), S(2), W(3)
# move = [북, 동, 남, 서]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

count = 1
turn = 0
while True:
    #step1
    turn_left()

    a = A + dx[d]
    b = B + dy[d]

    if visit[a][b] == 0 and game_map[a][b] == 0:
        visit[a][b] = 1
        A, B = a, b
        count += 1
        turn = 0
        continue
    else:
        # 이미 가봄 or 바다
        turn += 1

    if turn == 4:
        # 모든 방향 다 못감
        # 바라보는 방향 유지한 채로 뒤로 이동
        a = A - dx[d]
        b = B - dy[d]
        if game_map[a][b] == 0:
            A, B = a, b
        else:
            # 뒤도 바다
            break
        # turn 초기화
        turn = 0

print(count)

