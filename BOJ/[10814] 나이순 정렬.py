import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    a, n = input().split()
    a = int(a)
    arr.append([a, n, i])

arr.sort(key=lambda x:(x[0], x[2]))

for a, n, i in arr:
    print(a, n)