# 1. s의 각 문자를 index만큼 넘긴다.
# 1-1. skip문자 제외를 위해 index를 각각 넘긴다.
# 1-2. 아스키코드 활용
# 2. #1 반복 후 결과 출력

def solution(s, skip, index):
    skipOrd = set()
    for sk in skip:
        skipOrd.add(ord(sk))
        
    ans = []
    for i in (range(len(s))):
        ordS = ord(s[i])
        cnt = 0
        while cnt < index:
            ordS += 1
            if ordS > 122: 
                ordS = 97
            if ordS in skipOrd: continue
            cnt += 1
            
        ans.append(chr(ordS))
    
    return ''.join(ans)