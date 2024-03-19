import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = N - 1

result = [arr[-1], arr[-2]]
total = arr[-1] + arr[-2]
while start <= end:

    sum = arr[start] + arr[end]
    if abs(sum) < total:
        total = abs(sum)
        result = [arr[start], arr[end]]

    if sum < 0:
        start += 1
    else:
        end -= 1

print(*result)