from itertools import permutations


def solution(k, dungeons):
    # 8개밖에 안되니까 무조건 완탐 (8!도 작다.)

    perms = list(permutations(dungeons, len(dungeons)))
    max_cnt = 0
    for perm in perms:
        cnt = 0
        now = k
        for p in perm:
            if now < p[0]:
                break
            cnt += 1
            now -= p[1]

        if max_cnt < cnt:
            max_cnt = cnt

    return max_cnt