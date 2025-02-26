N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
# print(arr[: 2])

ans = (arr[0] * K + arr[1]) * M // (K + 1) + arr[0] * (M % (K + 1))

print(ans)

# 5 8 3
# 2 4 5 4 6