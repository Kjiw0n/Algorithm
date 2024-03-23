# 설탕 봉지는 3 or 5 킬로그램

N = int(input())

# 5x + 3y로 표현할 수 없다면 -1 출략

max_turn = N // 5
result = N + 1
for i in range(max_turn + 1):
    if (N - 5 * i) % 3 == 0:
        # print('i, (N - 5 * i) // 3: ', i, (N - 5 * i) // 3)
        temp = i + (N - 5 * i) // 3
        if result > temp:
            result = temp

if result == N + 1:
    print(-1)
else:
    print(result)