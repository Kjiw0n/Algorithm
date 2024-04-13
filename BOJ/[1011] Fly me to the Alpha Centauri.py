# 이동거리 급격하게 늘리면 안됨
# k 이동했으면 다음 턴에는 k-1, k, k+1
# -> 처음 작동 시엔 -1, 0, 1 (음수 혹은 0 이동은 의미 x)
# --> 처음 작동 시엔 1 이동
#
# 작동 시의 에너지 소모 큼
# -> 최소의 작동횟수 (!!)
#
# - 도착 바로 직전 이동거리 반드시 1
#

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    d = 1
    count = 0
    while x < y:
        print('x, y: ', x, y, 'd: ', d, 'count: ', count)
        x += d
        count += 1
        if x >= y:
            break

        y -= d
        count += 1

        if x >= y:
            break

        d += 1

    print(count)
