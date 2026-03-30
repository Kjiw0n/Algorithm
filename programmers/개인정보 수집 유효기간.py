# Todo: 유효기간이 지나 파기해야하는 개인정보 찾기
# return: 파기해야하는 개인정보 번호 배열 오름차순 정렬 후 리턴

# 1. 각 개인정보 별로 유효기간 체크
# 1-1. 약관 종류에 따라 유효기간 확인
# 1-2. 연/월/일 전부 일로 변환 (모든 달은 28일까지)
# 1-3. 유효기간 지난 개인정보 번호 저장해두기
# 2. 저장된 파기할 개인정보 번호 정렬

def solution(today, terms, privacies):
    terms_dict = {}
    for term in terms:
        type, period = term.split(' ')
        terms_dict[type] = int(period)
        
    Y, M, D = today.split('.')
    Y, M, D = int(Y), int(M), int(D)
    today = Y * 12 * 28 + M * 28 + D
    
    ans = []
    for i, privacie in enumerate(privacies):
        date, type = privacie.split(' ')
        y, m, d = date.split('.')
        y, m, d = int(y), int(m), int(d)
        period = terms_dict[type]
        
        expiredDate = y * 12 * 28 + (m + period) * 28 + d
        
        if expiredDate <= today:
            ans.append(i + 1)
        
    return ans