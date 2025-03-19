from itertools import combinations

# arr: 142506개
# 142506 * 10 * 5
# 무조건 가능

def solution(n, q_list, ans_list):
    arr = list(range(1, n + 1))
    arr = list(combinations(arr, 5))

    cnt = 0
    for a in arr:
        flag = True
        for q, ans in zip(q_list, ans_list):
            if ans != len(set(q) & set(a)):
                flag = False
                break
        if flag:
            cnt += 1

    return cnt