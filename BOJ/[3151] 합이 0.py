# 합이 0이 되는 3인조 경우의 수 리턴

# 1. 입력된 코딩 실력 순서대로 정렬 후, 차례대로 기준 값 설정
# 2. 기준 값 바로 다음 값(s), 맨 마지막 값(e) 조정해가며 합이 0인 경우 찾기
# 2-1. 중복 값의 경우 s~e 사이에 중복값 개수 찾기

# N = 10^4, O(N^2)

import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 0

for i in range(N):
    s, e = i + 1, N - 1
    while s < e:
        sum_val = arr[i] + arr[s] + arr[e]

        if sum_val == 0:
            if arr[s] == arr[e]:
                n = e - s + 1
                cnt += (n * (n - 1)) // 2
                break
            else:
                cnt_l, cnt_r = 0, 0
                l, r = arr[s], arr[e]
                while s < e and arr[s] == l:
                    cnt_l += 1
                    s += 1
                while s <= e and arr[e] == r:
                    cnt_r += 1
                    e -= 1
                cnt += (cnt_l * cnt_r)

        elif sum_val < 0:
            s += 1
        else:
            e -= 1

print(cnt)
