def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    pattern = [p1, p2, p3]

    # 생각해보니까 굳이 각 학생의 배열은 만들어 줄 필요가 없다.
    # pattern이랑 answers 바로 비교 후 cnt 계산하기
    cnt = []
    for p in pattern:
        c = 0
        for i, a in enumerate(answers):
            if a == p[i % len(p)]:
                c += 1
        cnt.append(c)

    M = max(cnt)
    answer = []
    for i in range(len(cnt)):
        if cnt[i] == M:
            answer.append(i + 1)

    return answer