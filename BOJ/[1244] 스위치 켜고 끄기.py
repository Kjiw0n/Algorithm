N = int(input())
arr = list(map(int, input().split()))
M = int(input())

def men(n):
    for i in range(n - 1, N, n):
        arr[i] = 1 - arr[i]
    return

def women(n):
    left = n - 1
    right = n - 1
    while left >= 0 and right < N and arr[left] == arr[right]:
        left -= 1
        right += 1
        print('left, right: ', left, right)
    for i in range(left + 1, right):
        arr[i] = 1 - arr[i]
    return

for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        # 남자
        men(b)
    else:
        # 여자
        women(b)
    # print(*arr)


# 20개씩 출력 처리 해줘야함
for i in range(0, N, 20):
    print(' '.join(map(str, arr[i:i+20])))


# 1 2 3 4 5 6 7 8
# 0 1 0 1 0 0 0 1
#
# 0 1 1 1 0 0 0 1
# 1 0 0 0 1 0 0 1
