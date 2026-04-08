# 조카 1명에게 줄 수 있는 막대 과자의 최대 길이 리턴

# 1. 시작점은 0, 끝점은 과자 최대 길이
# 2. 이진탐색으로 서치, 매번 중간값으로 조건 충족 가능한 지 반복문으로 확인

# N = 10^6, L = 10^9, O(N logL)

import sys

input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

h = 0
s, e = 1, max(arr)
while s <= e:
    mid = (s + e) // 2

    cnt = 0
    for a in arr:
        if a < mid: break
        cnt += (a // mid)
        if cnt >= M: break

    if cnt >= M:
        s = mid + 1
        h = mid
    else:
        e = mid - 1

print(h)