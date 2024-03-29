T = int(input())

for _ in range(T):
    N, arr = map(str, input().split())

    N = int(N)
    arr = list(arr)

    result = ''
    for a in arr:
        result += a * N

    print(result)