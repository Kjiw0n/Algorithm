import sys

input = sys.stdin.readline # 이거 없으면 시간초과

N, Q = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

prefix_sum = [0] * (N + 1) # l, r 인덱스랑 순서 맞춰주기 위해 +1만큼 초기화
prefix_sum[1] = arr[1]
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

for i in range(Q):
    l, r = map(int, input().split())
    print(prefix_sum[r] - prefix_sum[l - 1])
