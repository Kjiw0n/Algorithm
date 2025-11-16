from collections import deque

def solution(players, m, k):
    plus = deque()
    cnt = 0 # plus에 append 할 때마다 +1
    
    for i, player in enumerate(players):
        server = 1 + len(plus)
        if player >= m * server:
            # 증설 필요            
            # 몇 대 증설할건지 체크
            need = player // m
            for _ in range(need - server + 1):
                plus.append(k)
                cnt += 1
        
        for i in range(len(plus)):
            plus[i] -= 1
        while plus and plus[0] <= 0:
            plus.popleft()
        
    return cnt