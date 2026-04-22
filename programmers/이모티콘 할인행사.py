# 행사 목적(1. 가입자 수 증가, 2. 판매액 증가) 달성했을 때의 [이모플 가입자 수, 매출액] 리턴

# 1. 각 이모티콘 - 할인비율 조합 찾기 (4^7)
# 2. 각 조합 별로 users의 구매 결과 체크
# 2-1. 목표 1, 2에 부합하는 대로 결과 갱신
        
def solution(users, emoticons):
    perc = [10, 20, 30, 40]
    combs = []
    def dfs(comb, idx):
        if idx == len(emoticons):
            combs.append(comb)
            return
        for p in perc:
            dfs(comb + [p, emoticons[idx] * ((100 - p) / 100)], idx + 1)
    
    dfs([], 0)
    
    ans = [0, 0]
    for comb in combs:
        cnt, money = 0, 0 # comb의 총 결과
        for u_perc, u_limit in users:
            total = 0
            idx = 0
            while idx < len(comb):
                if u_perc <= comb[idx]:
                    total += comb[idx + 1]
                idx += 2
            if total >= u_limit:
                cnt += 1
            else:
                money += total
        if cnt > ans[0]:
            ans = [cnt, money]
        elif cnt == ans[0] and money > ans[1]:
            ans = [cnt, money]
        
    return ans