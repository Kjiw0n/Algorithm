# 무기 모두 만들기 위해 필요한 철의 무게 = 공격력 리턴

# 1. 기사번호 당 약수의 개수(공격력) 저장하기 (attacks)
# 1-1. 공격력이 제한 수치보다 큰 경우 정해진 공격력으로 저장
# 2. 총 공격력 리턴

def solution(number, limit, power):    
    divisors = [0] * (number + 1)
    
    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            divisors[j] += 1
    
    ans = 0
    for divisor in divisors:
        if divisor > limit:
            ans += power
        else:
            ans += divisor
    
    return ans