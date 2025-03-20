def solution(players, m, k):
    cnt = 0
    server = [[1, 100]]  # [늘어난 서버 개수, 서버 사용 가능 시간] # 기본서버 1개는 계속 돌아감
    for t, p in enumerate(players):
        s = sum(s[0] for s in server)  # 현재 돌아가는 서버 개수
        if p >= m * s:
            # 서버 증설 필요
            print('서버 증설 필요')
            rs = p // m - (s - 1)  # rs: required server
            cnt += rs
            server.append([rs, k])

        print(t, '시간대 ||', server)

        # 각 서버 사용시간 체크
        for i in range(len(server)):
            server[i][1] -= 1
        server = [s for s in server if s[1] != 0]

    return cnt