# s 13:13
# e 13:29 (16분)

N = int(input())
array = []
for i in range(N):
    x, y = map(int, input().split())
    array.append((x, y))

array.sort()

for i in range(N):
    print(*array[i])
