# 서로 다른 옷의 조합의 수 리턴

# 1. 종류별로 의상 분류
# 2. 각 종류에서 하나씩 꺼내서 조합
# 2-1. 안골라도 되니까 +1(빈 공간) 추가, 아무것도 안고르면 안되니까 전체 -1

from collections import Counter

def solution(clothes):
    cloth_nums = Counter(cloth_type for _, cloth_type in clothes)

    ans = 1
    for num in cloth_nums.values():
        ans *= (num + 1)
    
    return  ans - 1