# Todo: 주어진 명령어 수행하기, 행 삭제 여부 저장
# return: 주어진 명령어 모두 실행한 표, 처음 표 비교해서 삭제된 행 X, 삭제되지않은 행 O 표시하여 배열 리턴

# n ≤ 1,000,000(= N), cmd의 원소 개수 ≤ 200,000(= M)
# X는 1 이상 300,000 이하 (= T)
# cmd에 등장하는 모든 X들의 값을 합친 결과가 1,000,000 이하인 경우만 입력으로 주어집니다.
# -> N*M, M*T 안됨

# 1. 주어진 정보(행 개수, 선택된 행 위치) 바탕으로 표 저장
# 1-1. 각 행의 위/아래 정보 저장(up, down)
# 2. 명령어 실행
# 3. 처음 표와 명령어 실행 후 표 비교
# 3-1. 삭제된 행 X, 그렇지 않은 행 O 표기하여 리턴

def solution(n, k, cmd):
    up = [i - 1 for i in range(n)]
    down = [i + 1 for i in range(n)]
    idx = k
    deleted = []
    for c in cmd:
        if c[0] == 'U':
            d, x = c.split(' ')
            for _ in range(int(x)):
                idx = up[idx]
        elif c[0] == 'D':
            d, x = c.split(' ')
            for _ in range(int(x)):
                idx = down[idx]
        elif c[0] == 'C':
            
            deleted.append(idx)
            upIdx = up[idx] # 3
            downIdx = down[idx] # 5
            
            if upIdx != -1:
                down[upIdx] = downIdx
            if downIdx != n:
                up[downIdx] = upIdx
            
            if downIdx == n:
                idx = upIdx
            else:
                idx = downIdx
            
        elif c[0] == 'Z':
            i = deleted.pop()
            upIdx = up[i] # 3
            downIdx = down[i] # 5
            if upIdx != -1:
                down[upIdx] = i
            if downIdx != n:
                up[downIdx] = i
    
    ans = ['O'] * n
    for i in deleted:
        ans[i] = 'X'
    return ''.join(ans)