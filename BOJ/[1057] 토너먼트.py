N, a, b = map(int, input().split())

if a > b:
    a, b = b, a

cnt = 1
while a != b:
    if a % 2 != 0 and b - a == 1:
        print(cnt)
        exit()
    else:
        a = (a + 1) // 2
        b = (b + 1) // 2
        N = (N + 1) // 2
        # print(a, b, N)
    cnt += 1

print(-1)