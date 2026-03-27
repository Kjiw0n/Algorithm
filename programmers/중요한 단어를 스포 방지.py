# Todo: 스포 방지 단어 중, 중요한 단어 개수 찾기
# return: 중요한 단어의 수

# 1. 메세지에서 공백 기준으로 한 단어 씩 판단하기
# 1-1. 공백이 나타나기 전까지 한 단어로 처리
# 1-2. spoiler_ranges에 포함된 인덱스부터 flag 처리
# 2. 일반 단어 / 스포 방지 단어 구분해서 저장하기
# 2-1. 얘네는 set으로 저장하여 #3 수행 전에 차집합 적용하기
# 3. 구분 후에, 중요한 단어만 따로 저장
# 3-1. 중요한 단어도 set으로 저장하여 중복 제거

# N(message)이 20,000이므로 O(N)까지만 가능
# 시간복잡도: O(N)

def solution(message, spoiler_ranges):    
    N = len(message)
    spoiler_char = [False] * N
    for start, end in spoiler_ranges:
        for i in range(start, end + 1):
            spoiler_char[i] = True
    
    normal = set()
    spoiler = set()
    word = ''
    flag = False
    for i, m in enumerate(message): 
        if m != ' ': 
            word += m
            if spoiler_char[i]: flag = True
        elif word != '' and m == ' ':
            if flag: spoiler.add(word)
            else: normal.add(word)
            word = ''
            flag = False
    
        if i + 1 == N:
            if flag: spoiler.add(word)
            else: normal.add(word)
            
    important = spoiler - normal
    
    return len(important)