# 거스름돈은 5, 2원짜리밖에 없으니까 짝/홀 구분해서 계산
# 2의 배수일 때, 5의 배수일 때 나눠서 계산?
# 2의 배수일 땐 일반적인 방식 사용
# 5의 배수일 땐 charge[0]의 몫만 생각
# 근데 차피 거스름돈 2개니까 걍 묶어서 처리
# 2, 5의 배수 x일땐 ?
# 만약 5로 나눈 나머지가 홀수일 땐 5 한번 더해주기
# 만약 5로 나눈 나머지가 짝수일 땐 기존 로직과 같이 계산
# => 그럼 걍 '만약 5로 나눈 나머지가 홀수'인 경우만 생각

import sys

n = int(sys.stdin.readline())

charge = [5, 2]
count = [0] * len(charge)
count[0] = n // charge[0]
remain = n % 5

if remain == 0:
    print(sum(count))
else:
    while count[0] >= 0:
        if remain % 2 == 0:
            count[1] = remain // 2
            print(sum(count))
            break
        count[0] -= 1
        remain += 5
    else:
        print(-1)