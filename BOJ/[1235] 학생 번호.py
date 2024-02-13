# 이정도는 for문 계속 돌려도 될거같은데
# 뒤에 다 자르고 난 후의 집합의 원소 개수가 N이랑 같으면 break
# (실패 이유) 학생 번호가 무조건 7자리가 아닌가보다

N = int(input())
student_N = [input().strip() for _ in range(N)]

for j in range(1, len(student_N[0]) + 1):
    result = set()
    for n in student_N:
        result.add(n[-j:])
    if len(result) == N:
        print(j)
        break
