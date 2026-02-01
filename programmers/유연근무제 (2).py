def timeFunc(t):
    h = t // 100
    m = t % 100

    return h * 60 + m


def solution(schedules, timelogs, startday):
    n = len(schedules)
    for schedule, timelog in zip(schedules, timelogs):
        schedule = timeFunc(schedule)
        isLate = False
        day = startday

        for time in timelog:
            if day <= 5:
                time = timeFunc(time)
                if time > schedule + 10:
                    n -= 1
                    break

            day += 1
            if day > 7:
                day = 1

    return n