import sys
input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    arr.append(input().strip())

arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key=len)

for a in arr:
    print(a)


