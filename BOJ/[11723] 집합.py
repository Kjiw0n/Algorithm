import sys

input = sys.stdin.readline

M = int(input())

arr = [0] * 21
for i in range(M):
    s = input().strip()
    t = s.split(' ')
    if t[0] == 'add':
        arr[int(t[1])] = 1
    elif t[0] == 'remove':
        arr[int(t[1])] = 0
    elif t[0] == 'check':
        if arr[int(t[1])]:
            print(1)
        else:
            print(0)
    elif t[0] == 'toggle':
        if arr[int(t[1])]:
            arr[int(t[1])] = 0
        else:
            arr[int(t[1])] = 1
    elif t[0] == 'all':
        arr = [1] * 21
    elif t[0] == 'empty':
        arr = [0] * 21