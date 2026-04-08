# k번 파이프 열었다 닫은 후, 감염된 배양채 개수의 최댓값 리턴

# 1. 각 파이프(A, B, C) 하나씩 열기
# 2. edges 순회하며 연결된 노드 감염시키기
# 2-1. 감염된 노드들은 집합(infections)에 저장
# 2-3. 열 때마다 k--, k가 0이 될 때까지 반복, k와 infections, type 전달
# 3. 다시 백해서 다른 파이프 열고 #1부터 반복

# 백트래킹
# N = 100(: 배양체 개수), K = 10(: 행동), M = 3(: 파이프 종류) -> O(M^K * (N + N))

from collections import deque

def bfs(n, infections, graph, open): # 트리 전체 탐색하며 노드 감염시키는 역할
    queue = deque(infections)
    visited = [False] * (n + 1)
    for node in infections:
        visited[node] = True
    new = set()
    
    while queue:
        q = queue.popleft()
        new.add(q)
        for node, type in graph[q]:
            if not visited[node] and open == type:
                queue.append(node)
                visited[node] = True
    return new
    

def dfs(n, infections, k, graph):
    if k <= 0 or len(infections) == n:
        return len(infections)
        
    max_cnt = len(infections)
    
    for open in range(1, 4):
        new = bfs(n, infections, graph, open)
        if len(new) == len(infections): continue
        cnt = dfs(n, new, k - 1, graph)
        max_cnt = max(max_cnt, cnt)
    
    return max_cnt

def solution(n, infection, edges, k):
    graph = [[] for _ in range(n + 1)]
    for x, y, type in edges:
        graph[x].append((y, type))
        graph[y].append((x, type))
    
    infections = {infection}
    
    return dfs(n, infections, k, graph)