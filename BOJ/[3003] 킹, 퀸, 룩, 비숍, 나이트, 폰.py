piece = list(map(int, input().split()))

answer = [1, 1, 2, 2, 2, 8]

result = []
for i in range(6):
    result.append(answer[i] - piece[i])
print(*result)