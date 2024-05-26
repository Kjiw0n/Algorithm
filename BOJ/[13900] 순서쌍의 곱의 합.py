import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0
total = 0
for i in range(N):
    result += arr[i] * total
    total += arr[i]

print(result)