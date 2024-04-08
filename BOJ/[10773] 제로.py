import sys

input = sys.stdin.readline

K = int(input())

arr = []
for _ in range(K):
    n = int(input())
    if n != 0:
        arr.append(n)
    else:
        arr.pop()

print(sum(arr))