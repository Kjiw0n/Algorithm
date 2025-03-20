def solution(n, w, num):
    graph = []
    i = 1
    flag = False
    while i <= n:
        g = []
        for _ in range(w):
            if i > n:
                g.append(0)  # 0은 없다고 치자
            else:
                g.append(i)
            i += 1
        if flag:
            g.reverse()
        graph.append(g)
        flag = not flag

    graph.reverse()
    loc = [0, 0]
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == num:
                loc = [i, j]

    # i 위에 0박스 있는 지 체크 (맨 위만 보면 됨)
    if graph[0][loc[1]] == 0:
        return loc[0]
    else:
        return loc[0] + 1