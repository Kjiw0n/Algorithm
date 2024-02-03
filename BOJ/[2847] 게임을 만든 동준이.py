import sys

N = int(sys.stdin.readline())

score = [0] * N

for i in range(N):
    score[i] = int(sys.stdin.readline())

# 마지막 점수 기준으로
# -1 씩 낮아지면 됨

result = 0

for i in range(N - 2, -1, -1):
    if score[i] >= score[i + 1]:
        # score[i]은 score[i+1] - 1이 되어야함
        result += score[i] - (score[i + 1] - 1)
        score[i] = score[i + 1] - 1

print(result)