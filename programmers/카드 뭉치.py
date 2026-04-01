# 카드 뭉치에서 카드 한장 씩 뽑아서 문자열 만들기, 가능하면 Yes 아니면 No 리턴

# 1. goal의 단어를 순서대로 체크
# 2. cards1, cards2 중 단어가 있는 곳 체크
# 2-1. cards1에 단어가 있다면 해당 단어 사용
# 2-2. 없다면 cards2 확인
# 2-3. 둘 다 없다면 바로 No 리턴

def solution(cards1, cards2, goal):
    idx1 = 0
    len1 = len(cards1)
    idx2 = 0
    len2 = len(cards2)
    for s in goal:
        if idx1 < len1 and s == cards1[idx1]:
            idx1 += 1
        elif idx2 < len2 and s == cards2[idx2]:
            idx2 += 1
        else:
            return 'No'
        
    return 'Yes'