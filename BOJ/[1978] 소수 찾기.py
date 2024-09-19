N = int(input())
arr = list(map(int, input().split()))

cnt = 0
for a in arr:
    for i in range(2, a + 1):
        if a % i == 0:
            if i == a:
                cnt += 1
            break

print(cnt)
