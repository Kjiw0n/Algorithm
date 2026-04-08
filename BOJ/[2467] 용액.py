# 시작점을 처음, 끝점을 특성값의 최댓값

# 1. 입력된 용액의 순서대로 비교군을 잡고, 0에 가까운 용액을 찾는다. (반복)
# 2. n1을 제외한 용액들을 비교하며 혼합 특성값이 0에 가장 가까운 용액을 찾는다. (이분탐색)

# N = 10^5, O(N * logN)

N = int(input())
arr = list(map(int, input().split()))

ans = [arr[0], arr[N - 1]]
tot = abs(arr[0] + arr[N - 1])

for i in range(N):
    s, e = i + 1, N - 1
    while s <= e:
        mid = (s + e) // 2
        sum_value = arr[i] + arr[mid]

        if abs(sum_value) < tot:
            ans = [arr[i], arr[mid]]
            tot = abs(sum_value)

        if sum_value < 0:
            s = mid + 1
        else:
            e = mid - 1

print(*ans)
