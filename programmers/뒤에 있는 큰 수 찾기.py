# 각 원소의 뒷 큰수 찾아서 리턴

# 1. 원소 탐색할 때마다 뒷큰수 여부 찾기
# 2. 뒷큰수 못찾은 원소 인덱스는 스택에 저장
# 2-1. 스택의 마지막 값이 n보다 작은 경우만 whlie문, 뒤에서부터 pop -> ans
# 3. ans는 -1로 초기화, 끝까지 뒷큰수 못찾은 경우 자동으로 -1

# N = 10^6, O(N)

def solution(numbers):
    ans = [-1] * len(numbers)
    stack = []
    
    for i, n in enumerate(numbers):
        while stack and stack[-1][1] < n:
            idx, num = stack.pop()
            ans[idx] = n
        
        stack.append((i, n))
    
    return ans