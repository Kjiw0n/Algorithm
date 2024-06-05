import sys
input = sys.stdin.readline

n = int(input())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))

ps2 = [0] * (n - 1)
ps3 = [0] * (n - 1)
ps2[0], ps3[0] = arr2[0], arr3[0]

for i in range(1, n - 1):
    ps2[i] = ps2[i - 1] + arr2[i]

for i in range(1, n - 1):
    ps3[i] = ps3[i - 1] + arr3[i]

# print('p2: ', ps2)
# print('p3: ', ps3)

# ps[0] = arr2[0~-1] + arr1[0] + arr3[0~]
# ps[1] = arr2[0~0] + arr1[1] + arr3[1~]
# ps[2] = arr2[0~1] + arr1[2] + arr3[2~]

ps = [0] * n

min_index = 0

ps[0] = arr1[0] + ps3[n - 2]

for i in range(1, n):
    ps[i] = ps2[i - 1] + arr1[i] + ps3[n - 2] - ps3[i - 1]
    if ps[i] < ps[min_index]:
        min_index = i

# print(ps)
print(min_index + 1, min(ps))