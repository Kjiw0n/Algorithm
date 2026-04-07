# 과제를 끝난 순서대로 이름 담아서 배열 리턴

# 1. 과제 시작 시간은 분으로 표시한다.
# 2. 과제를 시작 시간 순으로 정렬한다.
# 3. 과제 시작 시간부터 진행하고, 다음 과제를 시작하기 전에 못끝냈으면 따로 저장해둔다.
# 3-1. 이때 가장 최근에 멈춘 과제부터 시작하므로 스택으로 저장한다.
# 3-2. 멈춘 과제와 새로운 과제가 있다면 새로운 과제를 우선으로 진행한다.
# 4. 다음 과제가 있다면, 다음 과제 시작 시간 전까지만 시행
# 4-1. 다음 과제가 없다면, 남아있는 거 최근 순으로 추가하면 됨

def solution(plans):
    for i, plan in enumerate(plans):
        h, m = map(int, plan[1].split(':'))
        plans[i][1] = h * 60 + m
        plans[i][2] = int(plan[2])
    plans.sort(key=lambda x: x[1])
    
    N = len(plans)
    
    ans = []
    remains = []
    for i in range(N - 1):
        t = plans[i][1]
        next = plans[i + 1][1] # 다음 과제 시작 시간
        if next - t >= plans[i][2]:
            # 과제 완료
            ans.append(plans[i][0])
            remain_t = next - t - plans[i][2]
        else:
            # 과제 남음
            plans[i][2] -= (next - t)
            remains.append(plans[i])
            remain_t = 0

        while remain_t > 0 and remains:
            remain = remains.pop()
            if remain_t >= remain[2]:
                remain_t -= remain[2]
                ans.append(remain[0])
            else:
                remain[2] -= remain_t
                remain_t = 0
                remains.append(remain)
    
    # 과제 완료, 시간 고려 x
    ans.append(plans[N-1][0])
    while remains:
        remain = remains.pop()
        ans.append(remain[0])
        
    return ans