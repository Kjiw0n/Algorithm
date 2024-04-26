import sys

input = sys.stdin.readline

N = int(input())

arr = [0] * 10001
for i in range(N):
    n = int(input())
    arr[n] += 1

cnt = 0
for i in range(10001):
    if cnt > N:
        break
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
            cnt += 1