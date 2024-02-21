visited = [False] * 9

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

def dfs(graph, i, visited):
    visited[i] = True
    print(i, end = ' ')
    for j in graph[i]:
        if not visited[j]:
            dfs(graph, j, visited)

dfs(graph, 1, visited)