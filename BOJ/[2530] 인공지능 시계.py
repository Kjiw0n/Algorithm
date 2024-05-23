A, B, C = map(int, input().split())
D = int(input())

result = A * (60 * 60) + B * 60 + C
result += D
print(result // (60 * 60) % 24, result % (60 * 60) // 60, result % 60)
