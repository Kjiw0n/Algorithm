# 게임판이 규칙을 지켰다면 1, 아니면 0 리턴

# 1. O -> X 표시 반복 중 실수
# 1-1. O의 개수가 X와 같거나 1 큰 경우 참
# 2. 게임 종료 후에도 게임 진행한 경우
# 2-1. 가로, 세로, 대각선 모두 확인 (8번)
# 2-2. 둘 다 참, O가 이겼는데 o != x+1, X가 이겼는데 o != x 이면 0 리턴

def isFinish(finish, board, p):
    for loc in finish:
        cnt = 0
        for i, j in loc:
            if board[i][j] == p: cnt += 1
        if cnt == 3: 
            return True
    return False

def solution(board):
    finish = [
        [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)], # 대각선
        [(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], # 가로
        [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]] # 세로
    
    board_str = "".join(board)
    o = board_str.count('O')
    x = board_str.count('X')
    
    if o < x or o > x + 1: return 0
    
    flag_o = isFinish(finish, board, 'O')
    flag_x = isFinish(finish, board, 'X')
    
    if (flag_o and flag_x) or (flag_o and o != x + 1) or (flag_x and o != x):
        return 0
            
    return 1