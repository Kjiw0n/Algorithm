import sys

input = sys.stdin.readline

arr_n = []
while True:
    n = int(input())
    if n == 0:
        break
    arr_n.append(n)

arr = [1 for i in range(max(arr_n) * 2 + 1)]
for n in arr_n:
    end = int((n * 2) ** (1/2))
    for i in range(2, end + 1):
        if arr[i] == 0:
            continue
        for j in range(i * i, n * 2 + 1, i):
            arr[j] = 0

    print(sum(arr[n + 1: 2 * n + 1]))

