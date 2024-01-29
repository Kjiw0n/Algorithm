import sys

N = int(sys.stdin.readline())

test = [0] * N
count = 0
score = 0

for i in range(N):
    test[i] = sys.stdin.readline()
    for j in range(len(test[i])):
        if test[i][j] == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)
    count = 0
    score = 0
