# 과일장수의 최대 이익 리턴

# 한 상자에 사과 m개씩 담을 때, 상자 가격 = 가장 낮은 점수 * m
# 1. 점수 오름차순으로 나열 후, 뒤에서부터 m개씩 자르기
# 2. 잘린 인덱스 - m + 1일때의 점수만 더하고, 마지막에 * m

def solution(k, m, score):
    score.sort()
    ans = 0
    for i in range(len(score) - 1, -1, -1 * m):
        if i >= m - 1:
            ans += score[i - m + 1]
    
    return ans * m