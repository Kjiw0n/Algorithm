N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(sorted(list(map(int, input().split()))))
# print(arr)

arr.sort(key=lambda x: -x[0])
print(arr[0][0])

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4