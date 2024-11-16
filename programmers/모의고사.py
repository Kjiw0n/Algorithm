def solution(answers):
    n = len(answers)
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    pattern = [p1, p2, p3]

    arr = []

    for p in pattern:
        N = n
        a = []
        if N >= len(p):
            a = p * (N // len(p))
            N %= len(p)

        a.extend(p[:N])
        arr.append(a)

    cnt = [0, 0, 0]
    for j in range(3):
        for i in range(n):
            if answers[i] == arr[j][i]:
                cnt[j] += 1

    M = max(cnt)
    answer = []
    for i in range(len(cnt)):
        if cnt[i] == M:
            answer.append(i + 1)

    return answer