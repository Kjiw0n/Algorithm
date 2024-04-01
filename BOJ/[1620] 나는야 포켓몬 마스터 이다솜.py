import sys

input = sys.stdin.readline

N, M = map(int, input().split())

name = {}
num = {}
for i in range(1, N + 1):
    s = input().strip()
    name[i] = s
    num[s] = i

for _ in range(M):
    s = input().strip()
    if s.isdigit():
        print(name[int(s)])
    else:
        print(num[s])
