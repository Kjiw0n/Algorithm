score = [int(input()) for _ in range(5)]

for i in range(5):
    score[i] = score[i] if score[i] >= 40 else 40

result = sum(score) // 5
# 주어지는 점수는 모두 5의 배수이므로 어차피 몫 = 나누기 값 동일함

print(result)