import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(str, input().split())))

for i in range(N):
    for j in range(1, 4):
        arr[i][j] = int(arr[i][j])

arr.sort()
arr.sort(key= lambda x: (-x[1], x[2], -x[3]))

for i in range(N):
    print(arr[i][0])