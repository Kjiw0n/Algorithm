# 모든 스테이지를 해결하는데 필요한 최소 비용

# 1. 각 스테이지의 힌트 개수를 저장하는 공간(hint_cnt) 만들기
# 2. 힌트 번들 구매/비구매 경우 나눠서 계산
# 3. 각 스테이지 진입 시, hint_cnt 통해 힌트 전부 사용할 시의 비용 치르기

# N = 16, K = 20, O(K * 2^N)

def dfs(cost, hint, n, k, hint_cnt, min_cost, idx):
    if idx == n - 1:
        return min_cost + cost[idx][min(hint_cnt[idx], n - 1)]
    
    # 힌트 비구매
    cur_cost = cost[idx][min(hint_cnt[idx], n - 1)]
    cost_no_buy = dfs(cost, hint, n, k, hint_cnt, min_cost + cur_cost, idx + 1)
    
    # 힌트 구매
    hint_cost = hint[idx][0]
    for i in range(1, k + 1):
        stage = hint[idx][i]
        hint_cnt[stage - 1] += 1
    cost_buy = dfs(cost, hint, n, k, hint_cnt, min_cost + cur_cost + hint_cost, idx + 1)
    for i in range(1, k + 1):
        stage = hint[idx][i]
        hint_cnt[stage - 1] -= 1
    
    return min(cost_no_buy, cost_buy)

def solution(cost, hint):
    n = len(cost)
    k = len(hint[0]) - 1
    hint_cnt = [0] * n
    
    min_cost = 0
    idx = 0 # 현재 진입한 스테이지 번호
    return dfs(cost, hint, n, k, hint_cnt, min_cost, idx)
