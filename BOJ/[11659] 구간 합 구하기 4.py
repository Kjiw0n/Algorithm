import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

prefix_sum = [0] * N
prefix_sum[0] = arr[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j - 1] - prefix_sum[i - 1] + arr[i - 1])
