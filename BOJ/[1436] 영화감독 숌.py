N = int(input())

n = 666
cnt = 0
while True:
    if '666' in str(n):
        cnt += 1
    if cnt == N:
        break
    n += 1

print(n)