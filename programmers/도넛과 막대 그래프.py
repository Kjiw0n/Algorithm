from collections import deque

def bfs(i, graph, N, visited, addedNode):
    # return donut -> 1, stick -> 2, 8 -> 3
    global node_cnt, edge_cnt
    queue = deque()
    queue.append(i)
    visited[i] = True
    while queue:
        t = queue.popleft()
        if t == addedNode: return 0
        if len(graph[t]) == 0:
            return 2
        elif len(graph[t]) == 2:
            return 3
        for nt in graph[t]:
            if not visited[nt]:
                visited[nt] = True
                queue.append(nt)
    return 1
    

def solution(edges):    
    N = max(max(u, v) for u, v in edges)
    graph = [[] for _ in range(N + 1)]
    find_max_edges = [0] * (N + 1)
    
    for u, v in edges:
        graph[u].append(v)
        find_max_edges[u] += 1
    
    addedNodes = []
    max_edge = max(find_max_edges)
    for i in range(1, N+1):
        if find_max_edges[i] == max_edge:
            addedNodes.append(i)
    
    # 이제 추가정점 건너뛰면서 그래프 순환해서 정점, 간선 개수에 따라 그래프형태 판별하면 됨
    for addedNode in addedNodes:
        pickedNodes = graph[addedNode] # 추가노드가 가리키는 노드들
        visited = [False] * (N + 1)
        
        ans = [addedNode, 0, 0, 0] # [addedNode, donut, stick, 8]
        
        for i in pickedNodes:
            res = bfs(i, graph, N, visited, addedNode)
            if res == 0:
                # res가 0일 때 -> 다음 addedNodes체크
                break
            ans[res] += 1
            
        else:
            return ans
        
    return [0, 0, 0, 0]