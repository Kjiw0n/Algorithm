# s 12:43 (20분)
# e 13:02

# 배열 A, B (각각 N개의 원소로 구성됨)
# 최대 K번 바꿔치기 가능
# 배열 A의 합이 최대가 되길 원함

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A 에서 가장 작은 원소 <-> B에서 가장 큰 원소
# A는 오름차순, B는 내림차순 정렬 후
# 같은 인덱스끼리 비교했을 때 A가 더 작으면 바꾸기, 바꿀 때 K -= 1
# A가 더 크면 -> 바꾸기 종료하고 출력

A = sorted(A)
B = sorted(B, reverse=True)

# sol1) 내가 푼 거
i = 0
while K > 0:
    if A[i] < B [i]:
        A[i], B[i] = B[i], A[i]
        K -= 1
    else:
        K = 0 # 반복 종료하겠다는거
    i += 1

# sol2) 책 풀이
for i in range(K):
    if A[i] > B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))