import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# 제일 큰 수랑 제일 작은 수 곱하면 됨
# 채점 프로그램은 B 재배열 여부를 모르지않나
sorted_A = sorted(A)
sorted_B = sorted(B, reverse=True)

min_S = 0

for i in range(N):
    min_S += sorted_A[i] * sorted_B[i]

print(min_S)