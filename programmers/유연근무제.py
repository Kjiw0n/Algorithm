def solution(schedules, timelogs, startday):
    schedules = [s + 10 for s in schedules]
    for i, s in enumerate(schedules):
        if s % 100 > 59:
            schedules[i] = ((s // 100) + 1) * 100 + s % 100 - 60
    ans = 0
    for s, times in zip(schedules, timelogs):
        cnt = 0
        d = startday
        for t in times:
            if d > 7:
                d = 1
            if d == 6 or d == 7:
                d += 1
                continue

            # 출근시간 검증 로직
            if t > s:
                break
            cnt += 1
            d += 1

        if cnt == 5:
            ans += 1

    return ans