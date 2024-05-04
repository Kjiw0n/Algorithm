from itertools import permutations

N = int(input())

arr = list(map(int, input().split()))

def check(arr, max_sum):
    sum = 0
    for i in range(1, N):
        sum += abs(arr[i - 1] - arr[i])

    if sum > max_sum:
        max_sum = sum

    return max_sum

perm = permutations(arr)

result = 0
for p in perm:
    result = check(p, result)

print(result)
