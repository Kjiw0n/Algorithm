# 숫자 -> 아스키코드: ord
# 아스키코드 -> 숫자: chr
# 문자 대문자화: upper
# 빈도 수: Counter
# for문 인자 두개 받아서 알파벳, 해당 알파벳의 빈도 수 한번에 처리

import sys
from collections import Counter

word = sys.stdin.readline().strip().upper()

counter = Counter(word)
max = max(counter.values())
result = []
for i, j in counter.items():
    if j == max:
        result.append(i)

if len(result) == 1:
    print(result[0])
else:
    print('?')
