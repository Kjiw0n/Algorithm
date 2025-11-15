def solution(diffs, times, limit):
    n = len(diffs)
    s, e = 1, max(diffs)
    ans = e
    while s <= e:
        level = (s + e) // 2
        
        now = times[0]
        for i in range(1, n):
            if diffs[i] > level:
                now += (diffs[i] - level) * (times[i] + times[i - 1])
            now += times[i]

        if now <= limit:
            ans = min(ans, level)
            e = level - 1
        else: 
            s = level + 1
        
    return ans