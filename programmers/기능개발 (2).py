from math import ceil


def solution(progresses, speeds):
    days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    ans = []
    max_day = days[0]
    cnt = 0
    for day in days:
        if day > max_day:
            ans.append(cnt)
            max_day = day
            cnt = 1
        else:
            cnt += 1

    ans.append(cnt)

    return ans