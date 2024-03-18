N = int(input())
arr = set(map(int, input().split()))
result = sorted(list(arr))

print(*result)