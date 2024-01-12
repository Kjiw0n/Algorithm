N, M = map(int, input().split())

result = N - M

if result >= 0:
    print(result)
else:
    print(-result)