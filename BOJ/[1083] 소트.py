import sys
# input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
S = int(input())

# (X) 가장 앞 인덱스부터 비교했을 때, 바로 뒤가 크다면 바꾸고, 더 작다면 바꾸지말고 다음으로 넘어감.
# 위에가 틀리는 이유는 양 옆에서 제일 큰 수 찾는 게 아니라 제일 큰 수를 앞으로 가져오는 게 우선이기 때문.
#
# !! 제일 큰 값을 앞으로 가져오기
# i = 0 부터 i = 남은 S 까지 중, 가장 큰 값 찾아서
# S -= max_index 해주고 해당 값 가져오기
# S > 0라면, 계속 반복
# 바꾸면 S -= 1
# if S <= 0: break

for i in range(N):
    max_A = max(A[i: min(N, i + S + 1)])
    max_index = A.index(max_A)

    for j in range(max_index, i, -1):
        n = A[j]
        A[j] = A[j - 1]
        A[j - 1] = n

    S -= max_index - i
    if S <= 0:
        break

for a in A:
    sys.stdout.write(str(a) + ' ')
