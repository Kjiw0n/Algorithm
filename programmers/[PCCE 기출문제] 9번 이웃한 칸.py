# 같은 색으로 칠해진 칸의 개수

def solution(board, h, w):
    n = len(board)
    cnt = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    for d in range(4):
        nh = h + dh[d]
        nw = w + dw[d]
        if 0 <= nh < n and 0 <= nw < n:
            if board[h][w] == board[nh][nw]:
                cnt += 1
    
    return cnt