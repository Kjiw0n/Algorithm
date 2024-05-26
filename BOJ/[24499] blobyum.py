import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr = arr + arr
print(arr)

prefix_sum = [0] * (2 * N + 1)
for i in range(2 * N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

print(prefix_sum)

result = 0
for i in range(K, 2 * N + 1):
    result = max(result, prefix_sum[i] - prefix_sum[i - K])

print(result)