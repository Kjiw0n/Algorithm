N = int(input())

cnt = 0
for _ in range(N):
    str1 = input()
    if str1[0] == 'C':
        cnt += 1

print(cnt)