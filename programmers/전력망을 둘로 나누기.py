from collections import defaultdict, deque


def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = True
    cnt = 1
    while queue:
        q = queue.popleft()
        for g in graph[q]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)
                cnt += 1
    return cnt


def solution(n, wires):
    min_diff = 99

    for i in range(len(wires)):
        graph = defaultdict(list)
        for j, (v1, v2) in enumerate(wires):
            if i == j:
                continue
            graph[v1].append(v2)
            graph[v2].append(v1)

        visited = [False] * (n + 1)
        # 전체 - (1번 wire와 연결되어있는 wire개수)
        f = bfs(1, graph, visited)
        e = n - f

        min_diff = min(min_diff, abs(f - e))

    return min_diff
