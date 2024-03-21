# 두 가지 함수 R(뒤집기)과 D(버리기)가 있다.

# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수이고,
# D는 첫 번째 수를 버리는 함수이다. 배열이 비어있는데 D를 사용한 경우에는 에러가 발생한다.
from collections import deque

T = int(input())
result = []

for t in range(T):
    P = input()
    n = int(input())
    arr = deque(input().strip('[]').split(','))

    if n == 0:
        arr = deque()

    r_count = 0
    for p in P:
        if p == 'R':
            r_count += 1
        elif p == 'D':
            if len(arr) > 0:
                if r_count % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                result.append('error')
                break
    if r_count % 2 != 0:
        arr.reverse()

    if len(result) == t:
        result.append('[' + ','.join(arr) + ']')

for r in result:
    print(r)
