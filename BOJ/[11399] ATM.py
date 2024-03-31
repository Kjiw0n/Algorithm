N = int(input())
arr = list(map(int, input().split()))

arr.sort()
total = 0
for i in range(N):
    total += sum(arr[:i + 1])

print(total)
