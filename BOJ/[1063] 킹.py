# 8 x 8 체스판
# 세로 대칭시켜서 생각하자

king = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

# 대칭시킨 버전은
# king = ['R', 'L', 'T', 'B', 'RB', 'LB', 'RT', 'LT']
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]
# 절대값은 (1, 0) (0, 1) (1, 1)

king_l, token_l, N = map(str, input().split())

# ord('A') = 65
king_l = [ord(king_l[0]) - 65, int(king_l[1]) - 1]
token_l = [ord(token_l[0]) - 65, int(token_l[1]) - 1]
N = int(N)

print('king_l, token_l: ', king_l, token_l)

game_route = []
for i in range(N):
    game_route.append(input())

print('game_route: ', game_route)

# (조건)
# 킹이나 돌이 체스판 밖으로 나갈 경우에는 그 이동은 건너 뛰고 다음 이동을 한다.
# 돌과 같은 곳으로 이동할 때는, 돌을 킹이 움직인 방향과 같은 방향으로 한 칸 이동시킨다. 아래 그림을 참고하자.
for game_r in game_route:
    i = king.index(game_r)
    print('i: ', i, 'game_r: ', game_r)
    kx = king_l[0] + dx[i]
    ky = king_l[1] + dy[i]
    king_m = [kx, ky]
    # (!!!!!!! )king_m, token_m으로 나눠야함. king의 움직임이 token에게 영향을 주는 경우에만 토큰도 움직이도록 처리
    turn = 0
    for m in king_m:
        # 킹이 체스판 밖으로 나가는 지 검사
        if m < 0 or m > 7:
            print('킹이 체스판 밖으로 나감') # 다 풀었으면 지워
            break
        turn += 1
    if turn == 2: # 킹이 전부 검사완료되었다면
        # 돌에게 영향 주는 지 확인
        print(king_m, token_l)
        if king_m == token_l:
            # 영향을 준다면
            print('킹이 돌한테 영향 줌')
            tx = token_l[0] + dx[i]
            ty = token_l[1] + dy[i]
            token_m = [tx, ty]
            for m in token_m:
                if m < 0 or m > 7:
                    print('돌이 체스판 밖으로 나감')  # 다 풀었으면 지워
                    # (!!!)돌이건 킹이건 하나라도 밖으로 나가면 해당 턴은 무효화임
                    break
                turn += 1
            if turn == 4:
                # 둘 다 체스판 밖으로 나가지 않는다면
                print('킹, 돌 모두 체스판 밖으로 안나감') # 다 풀었으면 지워
                king_l = [kx, ky]
                token_l = [tx, ty]
        else:
            king_l = [kx, ky]

result = []
result.append(chr(king_l[0] + 65) + str(king_l[1] + 1))
result.append(chr(token_l[0] + 65) + str(token_l[1] + 1))

print() # 지워
print('\n'.join(result))




# 아으아으아 뭔가 이상하다..