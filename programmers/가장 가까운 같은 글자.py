# return: 각 문자별로 앞에 가장 가까운 같은 글자의 위치를 저장한 배열, 같은 글자 없으면 -1 표시

# 1. a ~ z의 위치를 저장
# 1-1. 같은 문자 마주하면 위치 업데이트
# 2. 문자열 s 앞에서부터 순서대로 위치 확인하기

# N = 10,000(s의 길이), M = 26(알파벳 개수), O(M + N) => O(N)

def solution(S):
    arr = [-1] * 26 # 아스키코드 - 97로 위치 확인
    ans = []
    for i, s in enumerate(S):
        prev = arr[ord(s) - 97]
        if prev == -1:
            ans.append(-1)
        else:
            ans.append(i - prev)
        arr[ord(s) - 97] = i
    
    return ans