N = int(input())

N -= 1
temp = 6
cnt = 1
while N > 0:
    N -= temp
    cnt += 1

    temp += 6


print(cnt)