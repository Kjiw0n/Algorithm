def solution(friends, gifts):
    friends_dict = {friend: k for k, friend in enumerate(friends)}
    N = len(friends)
    graph = [[0] * N for _ in range(N)]  # 주고받은 선물
    graph2 = [0] * N  # 선물 지수
    gifts = [gift.split() for gift in gifts]
    for a, b in gifts:
        ai = friends_dict[a]
        bi = friends_dict[b]
        graph[ai][bi] += 1
        graph2[ai] += 1
        graph2[bi] -= 1

    ans = [0] * N
    for i in range(N):
        # i가 받을 선물의 개수 계산하기
        for j in range(N):
            # i와 j가 주고받은 기록 있는 지 체크
            if graph[i][j] == graph[j][i]:
                # 주고받은 기록이 없거나 주고받은 수가 같다면 -> 선물 지수 작은 사람 -> 선물 지수 큰 사람
                if graph2[i] > graph2[j]:
                    ans[i] += 1
                elif graph2[i] < graph2[j]:
                    ans[j] += 1
            else:
                # 주고받은 기록이 있다면, 더 많이 준 사람이 받음
                if graph[i][j] > graph[j][i]:
                    # i가 더 많이 줌
                    ans[i] += 1
                else:  # 같은 경우는 어차피 위에서 걸러진다.
                    ans[j] += 1

    return max(ans) // 2