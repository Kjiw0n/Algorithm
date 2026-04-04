# return: 부분 문자열이 나타내는 수가 p보다 작거나 같은 경우의 수

# 1. 부분 문자열의 길이(p의 길이) 저장해두기
# 2. 문자열 t를 첫번째 문자부터 (t의 길이 - p의 길이) 까지 순회하며 숫자 비교

# N = 10,000(t의 길이), M = 18(p의 길이) O(N * M)

def solution(t, p):
    partLen = len(p)
    cnt = 0
    for i in range(len(t) - partLen + 1):
        if t[i : i + partLen] <= p:
            cnt += 1
                
    return cnt