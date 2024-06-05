import sys
from itertools import permutations

input = sys.stdin.readline

def perm(s, n):
    # # n번째 부분만 순열 만들거임. 다 할 필요가 없음
    # s를 사전순으로 정렬했을 때
    # {n // factorial(len(s) - 1)} + 1
    #
    #
    # factorial(len(s) - 1) -> 한 세트에서 나올 수 있는 개수

    perm_list = []
    factorial = [1] * (len(s) + 1)
    for i in range(2, len(s) + 1):
        factorial[i] = factorial[i - 1] * i

    for i in range(len(s), 0, -1):
        fac = factorial[i - 1]
        index = n // fac
        perm_list.append(s[index])
        s.pop(index)
        n %= fac

    return ''.join(perm_list)


while True:
    arr = input().strip()
    if not arr:
        # 비어있으면
        break
    s, n = arr.split()
    n = int(n)

    fac_s = 1
    for i in range(1, len(s) + 1):
        fac_s *= i

    if n > fac_s:
        print(f"{s} {n} = No permutation")
    else:
        # 순열 직접 만들기
        print(f"{s} {n} = {perm(list(s), n - 1)}")
