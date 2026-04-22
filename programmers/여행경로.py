# 모든 항공권을 사용하는 경로 리턴

# 1. 각 공항 별 도착지 key-value(출발지 - (도착지, 티켓번호))로 저장
# 2. 각 공항 별로 가능한 도착지 방문하며 방문 경로 리턴
# 2-1. 모든 티켓 사용 시 경로 저장
# 3. 방문 경로가 여러 개면 사전 순 정렬 후 맨 앞 경로 리턴

from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for i, (s, e) in enumerate(tickets):
        graph[s].append((e, i))
    
    ans = []

    def dfs(visited, route, city):   
        if len(visited) == len(tickets):
            ans.append(route)
            return ans

        for des, i in graph[city]:
            if i not in visited:
                dfs(visited + [i], route + [des], des)
    
    dfs([], ['ICN'], 'ICN')
    ans.sort()
    
    return ans[0]