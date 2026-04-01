# 롤러로 페인트칠 해야 하는 최소 횟수 리턴

# 1. 다시 칠해야하는 구역을 순회 (이미 오름차순)
# 2. 롤러의 시작 지점, 끝 지점 판별
# 2-1. 롤러 사이에 있는 구역이면 패스, 그렇지 않으면 롤러 이동

# n = 100,000, O(n)

def solution(n, m, section):
    s = section[0]
    e = s + m
    cnt = 1
    for sec in section:
        if s <= sec < e:
            continue
        else:
            s = sec
            e = s + m
            cnt += 1
            
    return cnt