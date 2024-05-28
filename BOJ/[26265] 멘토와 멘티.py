import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(str, input().split())))


arr.sort(key=lambda x: x[1], reverse=True)
arr.sort(key=lambda x: x[0])

for a in arr:
    print(*a)
