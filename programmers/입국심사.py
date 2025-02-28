def solution(n, times):
    times.sort()

    ans = 0
    start = times[0]
    end = times[-1] * n
    while start <= end:
        mid = (start + end) // 2
        # mid 분 걸리면 해결 가능한가? -> mid분일때마다 사람 통과시켜보기.
        total = 0
        for t in times:
            total += (mid // t)
        # print(start, end, total, mid)
        if total >= n:
            ans = mid
            end = mid - 1
        else:
            start = mid + 1

    return ans