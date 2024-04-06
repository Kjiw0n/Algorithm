import sys

input = sys.stdin.readline

N, M = map(int, input().split())

s1 = set()
for _ in range(N):
    s1.add(input().strip())

s2 = set()
for _ in range(M):
    s2.add(input().strip())

result = s1 & s2

print(len(result))
for r in sorted(result):
    print(r)
