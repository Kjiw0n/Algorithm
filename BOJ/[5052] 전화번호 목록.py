import sys

input = sys.stdin.readline

T = int(input().strip())

for i in range(T):
    N = int(input().strip())
    arr = []
    for j in range(N):
        arr.append(input().strip())

    arr.sort(key=int)

    i = 0
    while 0 <= i < N:
        for k in range(i + 1, N):
            if arr[k].startswith(arr[i]):
                i = -100
                break
        i += 1

    if i < 0:
        print('NO')
    else:
        print('YES')

